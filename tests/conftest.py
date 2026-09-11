"""Unit tests must never activate a developer's deployment .env or real providers."""

import os

import pytest

from chapchap_customer_ai.core.settings import Settings, get_settings


@pytest.fixture(autouse=True)
def isolated_settings(monkeypatch):
    monkeypatch.setitem(Settings.model_config, "env_file", None)
    for key in os.environ:
        if key.startswith("CUSTOMER_AI_"):
            monkeypatch.delenv(key, raising=False)
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
