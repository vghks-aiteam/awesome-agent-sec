import copy
from datetime import date, timedelta
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import check_catalog as catalog


SCRIPT = Path(catalog.__file__).resolve()
PAPER = "https://arxiv.org/abs/2403.02691"
TOOL = "https://github.com/example/tool"


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.records = [
            {"title": "Example Paper", "url": PAPER, "kind": "paper", "publication_status": "unverified", "checked_on": "2026-01-01", "evidence_urls": [PAPER]},
            {"title": "Example Tool", "url": TOOL, "kind": "tool", "maintenance_status": "not_archived", "latest_release": None, "checked_on": "2026-01-01", "evidence_urls": [TOOL]},
        ]
        self.zh = f"# 資源\n\n[English](README.en.md)\n\n- [資料](#資料)\n\n## 資料\n\n- [Example Paper]({PAPER}) — 中文摘要。\n- [Example Tool]({TOOL}) — 中文工具說明。\n"
        self.en = f"# Resources\n\n[繁體中文](README.md)\n\n- [Items](#items)\n\n## Items\n\n- [Example Paper]({PAPER}) — English description.\n- [Example Tool]({TOOL}) — Tool description.\n"
        (self.root / "README.md").write_text(self.zh)
        (self.root / "README.en.md").write_text(self.en)
        (self.root / "docs").mkdir()
        (self.root / "docs/curation.md").write_text("[Home](../README.md)\n")
        self.write_data()

    def write_data(self):
        (self.root / "resources.json").write_text(json.dumps({"schema_version": 1, "resources": self.records}))
        (self.root / "RESOURCE_STATUS.md").write_text(catalog.render_status(self.records))

    def run_cli(self, *arguments):
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *arguments], capture_output=True, text=True)

    def test_valid_bilingual_catalog(self):
        self.assertEqual(catalog.validate(self.root), [])

    def test_title_with_em_dash_is_not_split(self):
        row = catalog.entries(f"## Test\n- [OAuth — RFC 9700](https://example.com) — Description.")[0]
        self.assertEqual(row[0], "OAuth — RFC 9700")

    def test_changed_english_order_is_rejected(self):
        lines = self.en.splitlines()
        lines[-2:] = reversed(lines[-2:])
        (self.root / "README.en.md").write_text("\n".join(lines))
        self.assertTrue(any("Catalogs differ" in error for error in catalog.validate(self.root)))

    def test_secondary_resource_drift_is_rejected(self):
        (self.root / "README.en.md").write_text(self.en.replace("Tool description.", "Tool description. [Paper](https://arxiv.org/abs/2406.11036)."))
        self.assertTrue(any("Catalogs differ" in error for error in catalog.validate(self.root)))

    def test_section_placement_drift_is_rejected(self):
        (self.root / "README.en.md").write_text(self.en.replace("- [Example Tool]", "## Another section\n\n- [Example Tool]"))
        self.assertTrue(any("Catalogs differ" in error for error in catalog.validate(self.root)))

    def test_duplicate_entries_are_rejected(self):
        for name in ["README.md", "README.en.md"]:
            file = self.root / name
            text = file.read_text()
            file.write_text(text + text.splitlines()[-1] + "\n")
        self.assertIn("Duplicate catalog entries", catalog.validate(self.root))

    def test_missing_metadata_is_rejected(self):
        self.records.pop()
        self.write_data()
        self.assertTrue(any("Metadata coverage mismatch" in error for error in catalog.validate(self.root)))

    def test_duplicate_metadata_is_rejected(self):
        self.records.append(copy.deepcopy(self.records[0]))
        self.write_data()
        self.assertIn("Duplicate metadata URLs", catalog.validate(self.root))

    def test_metadata_title_drift_is_rejected(self):
        self.records[0]["title"] = "Wrong title"
        self.write_data()
        self.assertTrue(any("Metadata title differs" in error for error in catalog.validate(self.root)))

    def test_published_paper_requires_publisher_evidence(self):
        self.records[0]["publication_status"] = "published"
        self.assertTrue(any("needs venue and evidence" in error for error in catalog.metadata_errors(self.records)))

    def test_future_check_dates_are_rejected(self):
        self.records[0]["checked_on"] = (date.today() + timedelta(days=1)).isoformat()
        self.assertTrue(any("Future check date" in error for error in catalog.metadata_errors(self.records)))

    def test_invalid_check_date_is_rejected(self):
        self.records[0]["checked_on"] = "unknown"
        self.assertTrue(any("Invalid check date" in error for error in catalog.metadata_errors(self.records)))

    def test_release_requires_version_evidence(self):
        self.records[1]["latest_release"] = "v1.0.0"
        self.assertTrue(any("Release needs URL and date" in error for error in catalog.metadata_errors(self.records)))

    def test_arxiv_cannot_bypass_publication_fields(self):
        self.records[0]["kind"] = "reference"
        self.assertTrue(any("must be a paper" in error for error in catalog.metadata_errors(self.records)))

    def test_stale_generated_report_is_rejected(self):
        (self.root / "RESOURCE_STATUS.md").write_text("old report\n")
        self.assertTrue(any("RESOURCE_STATUS.md is stale" in error for error in catalog.validate(self.root)))

    def test_broken_local_link_is_rejected(self):
        (self.root / "docs/curation.md").write_text("[Missing](../missing.md)\n")
        self.assertTrue(any("Missing local link" in error for error in catalog.validate(self.root)))

    def test_chinese_encoded_duplicate_heading_anchor(self):
        (self.root / "docs/curation.md").write_text("[第二節](#%E8%B3%87%E6%96%99-1)\n\n## 資料\n\n## 資料\n")
        self.assertEqual(catalog.validate(self.root), [])

    def test_example_links_inside_code_fences_are_ignored(self):
        (self.root / "docs/curation.md").write_text("```markdown\n[Example](missing.md)\n```\n")
        self.assertEqual(catalog.validate(self.root), [])

    def test_cli_generates_report_then_validates(self):
        (self.root / "RESOURCE_STATUS.md").unlink()
        result = self.run_cli("--write-status")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.run_cli().returncode, 0)

    def test_cli_rejects_broken_user_flow(self):
        (self.root / "README.en.md").write_text(self.en.replace(TOOL, "https://github.com/example/other"))
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("Catalogs differ", result.stdout)

    def test_real_repository_smoke(self):
        result = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
