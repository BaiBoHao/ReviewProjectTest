from __future__ import annotations

import unittest

from review_project_test.profile_loader import normalized_display_name


class ProfileLoaderTests(unittest.TestCase):
    def test_missing_display_name_uses_anonymous_fallback(self) -> None:
        self.assertEqual(normalized_display_name({}), "anonymous")


if __name__ == "__main__":
    unittest.main()
