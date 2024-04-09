import heapq


class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        max_deabts = self.get_max_deabts(
            open_contracts, renegotiated_contracts)

        top_n_open_contracts = self.get_top_n_max_deabts(max_deabts, top_n)

        return [contract[1] for contract in top_n_open_contracts]

    def get_max_deabts(self, open_contracts, renegotiated_contracts):
        max_deabts = [(-contract.debt, contract.id)
                      for contract in open_contracts if contract.id not in renegotiated_contracts]
        return max_deabts

    def get_top_n_max_deabts(self, max_debts, top_n):
        if len(max_debts) > top_n:
            max_debts = heapq.nsmallest(top_n, max_debts)
        return max_debts
