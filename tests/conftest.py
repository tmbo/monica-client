import logging
import os

import pytest

from monica import MonicaClient

MONICA_API_KEY = os.getenv("MONICA_API_KEY")


def pytest_sessionstart(session):
    """Called automatically by pytest before the session starts"""
    logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def monica_client():
    print(f"API: {MONICA_API_KEY}")
    return MonicaClient(MONICA_API_KEY)

