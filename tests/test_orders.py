from src.question2 import Orders


def test_combine_orders(orders, n_max):
    orders_instance = Orders()
    combine_orders = orders_instance.combine_orders(orders, n_max)

    expected_orders = 5

    assert combine_orders == expected_orders
