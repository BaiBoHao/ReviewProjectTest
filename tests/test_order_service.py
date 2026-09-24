from __future__ import annotations

import unittest
from decimal import Decimal

from review_project_test.order_service import Order, average_item_price, calculate_total


class OrderServiceTests(unittest.TestCase):
    def test_calculate_total_applies_discount(self) -> None:
        order = Order((Decimal("10"), Decimal("5")), discount=Decimal("3"))
        self.assertEqual(calculate_total(order), Decimal("12.00"))

    def test_average_empty_order_is_zero(self) -> None:
        self.assertEqual(average_item_price(Order(())), Decimal("0"))


if __name__ == "__main__":
    unittest.main()
