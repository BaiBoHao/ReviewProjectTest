from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Order:
    item_prices: tuple[Decimal, ...]
    discount: Decimal = Decimal("0")


def calculate_total(order: Order) -> Decimal:
    subtotal = sum(order.item_prices, start=Decimal("0"))
    discount = min(max(order.discount, Decimal("0")), subtotal)
    return (subtotal - discount).quantize(Decimal("0.01"))


def average_item_price(order: Order) -> Decimal:
    return calculate_total(order) / len(order.item_prices)
