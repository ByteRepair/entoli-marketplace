"""Collection keys on ext manifests and the collections.json record."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site
import fetch_remote

BASE = {"repo": "google/skills", "path": "skills"}


def result(*rels: str, **extra) -> fetch_remote.RemoteResult:
    return fetch_remote.RemoteResult(
        slug="google",
        section="skills",
        repo="google/skills",
        ref=None,
        path="skills",
        tags=None,
        entries=[
            fetch_remote.RemoteEntry(
                section="skills",
                slug="google",
                repo="google/skills",
                ref=None,
                path="skills",
                rel=rel,
            )
            for rel in rels
        ],
        authors=None,
        **extra,
    )


class CheckManifest(unittest.TestCase):
    def test_accepts_name_and_summary(self):
        manifest = {**BASE, "name": "Google", "summary": "Google's own skills."}
        self.assertEqual(fetch_remote.check_manifest("g", manifest), [])

    def test_rejects_empty_name(self):
        errors = fetch_remote.check_manifest("g", {**BASE, "name": "  "})
        self.assertEqual(len(errors), 1)
        self.assertIn('"name"', errors[0])

    def test_rejects_long_summary(self):
        errors = fetch_remote.check_manifest("g", {**BASE, "summary": "x" * 161})
        self.assertEqual(len(errors), 1)
        self.assertIn('"summary"', errors[0])


class CollectionRecord(unittest.TestCase):
    def test_sub_entries_make_a_collection(self):
        record = build_site.collection_record(
            result("gcs", "bigquery", name="Google", summary="Cloud.")
        )
        self.assertEqual(record, {"name": "Google", "summary": "Cloud."})

    def test_name_falls_back_to_slug(self):
        record = build_site.collection_record(result("gcs"))
        self.assertEqual(record, {"name": "google", "summary": ""})

    def test_single_entry_is_not_a_collection(self):
        self.assertIsNone(build_site.collection_record(result("", name="Google")))


if __name__ == "__main__":
    unittest.main()
