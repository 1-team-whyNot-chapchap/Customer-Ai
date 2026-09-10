"""PVC-backed idempotency for one process. Customer owns retry and business state."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from threading import RLock

from chapchap_customer_ai.consultation.idempotency import InMemoryConsultationResponseRegistry
from chapchap_customer_ai.consultation.models import ConsultationRequestError
from chapchap_customer_ai.contracts.models import ConsultationResponse
from chapchap_customer_ai.knowledge.models import JobRegistration, KnowledgeRequestError
from chapchap_customer_ai.summary.models import SummaryJobRegistration, SummaryRequestError


def claim_runtime_volume(directory: Path):
    """Hold until shutdown; refuse two workers using one embedded Chroma volume."""
    directory.mkdir(parents=True, exist_ok=True)
    handle = (directory / "runtime.lock").open("a+b")
    try:
        if os.name == "nt":
            import msvcrt

            handle.write(b"0")
            handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        handle.close()
        raise ValueError("Academy runtime volume already has an active worker") from None
    return handle


class RuntimeStore:
    def __init__(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "runtime.sqlite3"
        self.lock = RLock()
        with self.transaction() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kind TEXT NOT NULL, key TEXT NOT NULL, fingerprint TEXT NOT NULL,
                    external_id INTEGER, UNIQUE(kind, key), UNIQUE(kind, external_id)
                );
                CREATE TABLE IF NOT EXISTS attempts (
                    job_id INTEGER NOT NULL, attempt INTEGER NOT NULL,
                    done INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(job_id, attempt)
                );
                CREATE TABLE IF NOT EXISTS responses (
                    key TEXT PRIMARY KEY, fingerprint TEXT NOT NULL, response TEXT
                );
                CREATE TABLE IF NOT EXISTS pending (
                    kind TEXT NOT NULL, key TEXT NOT NULL, attempt INTEGER NOT NULL,
                    request_id TEXT NOT NULL, payload TEXT NOT NULL,
                    PRIMARY KEY(kind,key,attempt)
                );
            """)
        # Only in-flight ownership is ephemeral: a resent unfinished request can run again.
        self.running: set[tuple[int, int]] = set()

    def save_pending(self, kind, key, attempt, request_id, request):
        with self.transaction() as db:
            db.execute(
                "INSERT OR REPLACE INTO pending VALUES (?,?,?,?,?)",
                (kind, key, attempt, str(request_id), request.model_dump_json()),
            )

    def pending(self):
        with self.transaction() as db:
            return db.execute("SELECT kind,key,request_id,payload FROM pending").fetchall()

    @contextmanager
    def transaction(self):
        with self.lock:
            db = sqlite3.connect(self.path, timeout=10)
            try:
                with db:
                    yield db
            finally:
                db.close()


class PersistentKnowledgeJobRegistry:
    def __init__(self, store: RuntimeStore):
        self.store = store

    def record_request(self, key, request_id, request):
        self.store.save_pending("knowledge", key, request.attempt, request_id, request)

    def register(self, logical_key, fingerprint, attempt):
        if not logical_key or not fingerprint or not 1 <= attempt <= 3:
            raise ValueError("Invalid knowledge registration")
        with self.store.transaction() as db:
            row = db.execute(
                "SELECT id, fingerprint FROM jobs WHERE kind='knowledge' AND key=?", (logical_key,)
            ).fetchone()
            if row and row[1] != fingerprint:
                raise KnowledgeRequestError("Conflicting knowledge request", status_code=409)
            if row is None:
                cursor = db.execute(
                    "INSERT INTO jobs(kind,key,fingerprint) VALUES ('knowledge',?,?)",
                    (logical_key, fingerprint),
                )
                job_id = cursor.lastrowid
            else:
                job_id = row[0]
            done = db.execute(
                "SELECT done FROM attempts WHERE job_id=? AND attempt=?", (job_id, attempt)
            ).fetchone()
            identity = (job_id, attempt)
            schedule = identity not in self.store.running and (done is None or not done[0])
            if schedule:
                db.execute("INSERT OR IGNORE INTO attempts(job_id,attempt) VALUES (?,?)", identity)
                self.store.running.add(identity)
            return JobRegistration(job_id, schedule)

    def release_attempt(self, logical_key, attempt):
        self._finish(logical_key, attempt, False)

    def complete_attempt(self, logical_key, attempt):
        self._finish(logical_key, attempt, True)

    def _finish(self, key, attempt, done):
        with self.store.transaction() as db:
            row = db.execute(
                "SELECT id FROM jobs WHERE kind='knowledge' AND key=?", (key,)
            ).fetchone()
            if row:
                db.execute(
                    "UPDATE attempts SET done=? WHERE job_id=? AND attempt=?",
                    (int(done), row[0], attempt),
                )
                self.store.running.discard((row[0], attempt))
                if done:
                    db.execute(
                        "DELETE FROM pending WHERE kind='knowledge' AND key=? AND attempt=?",
                        (key, attempt),
                    )


class PersistentSummaryJobRegistry:
    def __init__(self, store: RuntimeStore):
        self.store = store

    def record_request(self, key, request_id, request):
        self.store.save_pending("summary", key, 1, request_id, request)

    def register(self, key, summary_job_id, fingerprint):
        if not key.strip() or summary_job_id <= 0 or not fingerprint:
            raise ValueError("Invalid summary registration")
        with self.store.transaction() as db:
            row = db.execute(
                "SELECT id,fingerprint,external_id FROM jobs WHERE kind='summary' AND key=?", (key,)
            ).fetchone()
            if row and (row[1] != fingerprint or row[2] != summary_job_id):
                raise SummaryRequestError("Conflicting summary request", status_code=409)
            if row is None:
                try:
                    cursor = db.execute(
                        "INSERT INTO jobs(kind,key,fingerprint,external_id) "
                        "VALUES ('summary',?,?,?)",
                        (key, fingerprint, summary_job_id),
                    )
                except sqlite3.IntegrityError:
                    raise SummaryRequestError(
                        "Conflicting summary job ID", status_code=409
                    ) from None
                job_id = cursor.lastrowid
            else:
                job_id = row[0]
            done = db.execute(
                "SELECT done FROM attempts WHERE job_id=? AND attempt=1", (job_id,)
            ).fetchone()
            identity = (job_id, 1)
            schedule = identity not in self.store.running and (done is None or not done[0])
            if schedule:
                db.execute("INSERT OR IGNORE INTO attempts(job_id,attempt) VALUES (?,1)", (job_id,))
                self.store.running.add(identity)
            return SummaryJobRegistration(schedule)

    def release(self, key, summary_job_id):
        self._finish(key, summary_job_id, False)

    def complete(self, key, summary_job_id):
        self._finish(key, summary_job_id, True)

    def _finish(self, key, external_id, done):
        with self.store.transaction() as db:
            row = db.execute(
                "SELECT id FROM jobs WHERE kind='summary' AND key=? AND external_id=?",
                (key, external_id),
            ).fetchone()
            if row:
                db.execute(
                    "UPDATE attempts SET done=? WHERE job_id=? AND attempt=1", (int(done), row[0])
                )
                self.store.running.discard((row[0], 1))
                if done:
                    db.execute("DELETE FROM pending WHERE kind='summary' AND key=?", (key,))


class PersistentConsultationResponseRegistry:
    def __init__(self, store: RuntimeStore):
        self.store = store
        self.inflight = InMemoryConsultationResponseRegistry()

    def execute_once(self, key, fingerprint, factory):
        def execute():
            with self.store.transaction() as db:
                row = db.execute(
                    "SELECT fingerprint,response FROM responses WHERE key=?", (key,)
                ).fetchone()
                if row:
                    if row[0] != fingerprint:
                        raise ConsultationRequestError(
                            "Conflicting consultation request", status_code=409
                        )
                    if row[1] is not None:
                        return ConsultationResponse.model_validate_json(row[1])
                else:
                    db.execute(
                        "INSERT INTO responses(key,fingerprint) VALUES (?,?)", (key, fingerprint)
                    )
            response = factory()
            with self.store.transaction() as db:
                db.execute(
                    "UPDATE responses SET response=? WHERE key=?", (response.model_dump_json(), key)
                )
            return response

        return self.inflight.execute_once(key, fingerprint, execute)
