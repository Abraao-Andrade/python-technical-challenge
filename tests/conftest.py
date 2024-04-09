import pytest
from src.question1 import Contract


@pytest.fixture(scope="session")
def contracts():
    return [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]


@pytest.fixture(scope="session")
def contracts_renegotiated():
    return [3]


@pytest.fixture(scope="session")
def top_n():
    return 3


@pytest.fixture(scope="session")
def orders():
    return [
        99,
        70,
        30,
        10,
        90,
        80,
        80,
        20,
        1,
    ]


@pytest.fixture(scope="session")
def n_max():
    return 100
