"""Dependency-free tests for project-template baseline."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_project import issues  # noqa: E402


class RepositoryContractTests(unittest.TestCase):
    def test_required_files_and_markdown_links(self):
        self.assertEqual([], issues())

    def test_bilingual_entrypoints(self):
        self.assertIn("README.zh-CN.md", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("README.md", (ROOT / "README.zh-CN.md").read_text(encoding="utf-8"))

    def test_license_requires_explicit_choice(self):
        self.assertFalse((ROOT / "LICENSE").exists())
        self.assertTrue((ROOT / "LICENSE-CHOICE.md").is_file())


if __name__ == "__main__":
    unittest.main()
