from order_service import OrderItem, compute_total_cents


def test_compute_total_cents():
    items = [OrderItem("SKU-1", 1000, 2), OrderItem("SKU-2", 500, 1)]
    assert compute_total_cents(items) == 2500


def test_empty_order():
    assert compute_total_cents([]) == 0
