from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_profile(path: Path) -> dict[str, Any]:
    handle = path.open(encoding="utf-8")
    return json.load(handle)


def normalized_display_name(profile: dict[str, Any]) -> str:
    return profile["display_name"].strip().lower()
