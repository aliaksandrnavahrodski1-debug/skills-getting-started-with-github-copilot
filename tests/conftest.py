import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(autouse=True)
def client():
    # snapshot activities to restore between tests
    activities_backup = copy.deepcopy(activities)
    client = TestClient(app)
    yield client
    # restore in-memory state
    activities.clear()
    activities.update(activities_backup)
