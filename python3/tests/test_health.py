from fastapi.testclient import TestClient
import json
from pathlib import Path
import server as app_module

client = TestClient(app_module.app)


def test_health_endpoint_returns_file_content():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()

    # Load expected content from file
    health_file = Path(__file__).resolve().parents[1] / "health.json"
    expected = json.loads(health_file.read_text(encoding="utf-8"))

    assert data == expected
