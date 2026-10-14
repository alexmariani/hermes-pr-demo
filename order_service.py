from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    sku: str
    price_cents: int
    qty: int


def compute_total_cents(items: list[OrderItem]) -> int:
    if not items:
        return 0
    return sum(i.price_cents * i.qty for i in items if i.qty > 0)
