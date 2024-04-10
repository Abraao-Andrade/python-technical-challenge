import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def sample_batch_request():
    return {
        "open_contracts": [
            {"id": 1, "debt": 70},
            {"id": 2, "debt": 30},
            {"id": 3, "debt": 10},
            {"id": 4, "debt": 90},
            {"id": 5, "debt": 80},
            {"id": 6, "debt": 80}
        ],
        "renegotiated_contracts": [{"id": 3}],
        "top_n": 3
    }


def test_get_top_n_open_contracts(sample_batch_request):
    response = client.post(
        "/contracts/get_top_n_open_contracts", json=sample_batch_request)
    response_data = response.json()

    assert response.status_code == 200
    assert "top_n_open_contracts" in response_data
    assert response_data.get("top_n_open_contracts") == [4, 5, 6]


def test_combine_orders():
    request_body = {
        "requests": [70, 30, 10, 90, 80],
        "n_max": 100
    }
    response = client.post("/orders/combine_orders", json=request_body)
    response_data = response.json()

    assert response.status_code == 200
    assert "num_trips" in response.json()
    assert response_data.get("num_trips") == 3
