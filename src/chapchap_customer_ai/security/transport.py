"""HTTPS by default; exact, operator-configured HTTP origin exceptions."""

from collections.abc import Collection
from urllib.parse import urlsplit


def allowed_url(url: str, http_origins: Collection[str] = (), *, origin_only=False) -> bool:
    try:
        parsed = urlsplit(url)
        if (
            not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.fragment
            or any(c.isspace() or ord(c) < 32 for c in url)
            or "\\" in url
            or (parsed.port is not None and parsed.port <= 0)
            or (origin_only and (parsed.path not in {"", "/"} or parsed.query))
        ):
            return False
        if parsed.scheme == "https":
            return True
        if parsed.scheme != "http":
            return False
        for origin in http_origins:
            candidate = urlsplit(origin)
            if (
                candidate.scheme == "http"
                and candidate.hostname
                and candidate.username is None
                and candidate.password is None
                and candidate.path in {"", "/"}
                and not candidate.query
                and not candidate.fragment
                and not any(c.isspace() for c in origin)
                and "\\" not in origin
                and (candidate.hostname, candidate.port or 80)
                == (parsed.hostname, parsed.port or 80)
            ):
                return True
    except (ValueError, TypeError):
        return False
    return False
