from src.question1 import Contracts


def test_get_top_N_open_contracts(contracts, contracts_renegotiated, top_n):
    contracts_instance = Contracts()
    actual_open_contracts = contracts_instance.get_top_N_open_contracts(
        contracts, contracts_renegotiated, top_n)

    expected_open_contracts = [5, 4, 2]

    assert expected_open_contracts == actual_open_contracts
