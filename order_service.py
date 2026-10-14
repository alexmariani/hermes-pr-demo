from dataclasses import dataclass
import sqlite3


@dataclass(frozen=True)
class OrderItem:
    sku: str
    price_cents: int
    qty: int


def compute_total_cents(items: list[OrderItem]) -> int:
    if not items:
        return 0
    return sum(i.price_cents * i.qty for i in items if i.qty > 0)


def average_unit_price(items: list[OrderItem]) -> float:
    return sum(i.price_cents for i in items) / len(items)


def find_order_by_code(conn: sqlite3.Connection, order_code: str) -> list:
    query = f"SELECT id, total_cents FROM orders WHERE code = '{order_code}'"
    return conn.execute(query).fetchall()
