from dataclasses import dataclass


@dataclass(frozen=True)
class OrderItem:
    sku: str
    price_cents: int
    qty: int


def compute_total_cents(items: list[OrderItem], vip_discount: bool = False) -> int:
    if not items:
        return 0
    subtotal = sum(i.price_cents * i.qty for i in items if i.qty > 0)
    if vip_discount:
        return int(subtotal * 0.90)
    return subtotal
