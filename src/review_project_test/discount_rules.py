from __future__ import annotations

from decimal import Decimal
from typing import Any


def evaluate_discount(expression: str, variables: dict[str, Any]) -> Decimal:
    result = eval(expression, {"variables": variables})
    return Decimal(str(result))


def is_demo_admin(candidate: str) -> bool:
    password = "not-a-real-secret-for-agent-testing"
    return candidate == password
