"""Regression checks for the optional profile activity refresh."""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

spec = importlib.util.spec_from_file_location(
    "profile_activity", Path(__file__).with_name("update_profile_activity.py")
)
activity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(activity)


class ProfileActivityTests(unittest.TestCase):
    def test_curated_readme_stays_unchanged_without_network(self):
        readme = Mock()
        readme.read_text.return_value = "# Matthew Paver\n\nSelected public work.\n"
        with patch.object(activity, "README_PATH", readme), patch.object(
            activity, "fetch_json", side_effect=AssertionError("Unexpected network request")
        ):
            self.assertEqual(activity.main(), 0)
        readme.write_text.assert_not_called()

    def test_incomplete_marker_pair_does_not_replace_content(self):
        readme = Mock()
        readme.read_text.return_value = activity.START_MARKER + "\nHand-written content.\n"
        with patch.object(activity, "README_PATH", readme), patch.object(
            activity, "fetch_json", side_effect=AssertionError("Unexpected network request")
        ):
            self.assertEqual(activity.main(), 0)
        readme.write_text.assert_not_called()

    def test_opted_in_block_keeps_surrounding_copy_and_excludes_private_repos(self):
        readme = Mock()
        readme.read_text.return_value = (
            "Intro\n" + activity.START_MARKER + "\nOld content\n"
            + activity.END_MARKER + "\nClosing\n"
        )
        repos = [
            {"name": "public-example", "private": False, "html_url": "https://example.com/public"},
            {"name": "private-example", "private": True},
            {"name": "fork-example", "private": False, "fork": True},
        ]
        with patch.object(activity, "README_PATH", readme), patch.object(
            activity, "fetch_json", return_value=repos
        ):
            self.assertEqual(activity.main(), 0)
        result = readme.write_text.call_args.args[0]
        self.assertTrue(result.startswith("Intro\n"))
        self.assertTrue(result.endswith("Closing\n"))
        self.assertIn("public-example", result)
        self.assertNotIn("private-example", result)
        self.assertNotIn("fork-example", result)
        self.assertNotIn("Old content", result)


if __name__ == "__main__":
    unittest.main()
