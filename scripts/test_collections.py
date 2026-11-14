"""Collections: ext manifests, collections/<section>.toml, and the merged record."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site
import collection_files
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
        self.assertEqual(
            record,
            {
                "name": "Google",
                "summary": "Cloud.",
                "members": ["google/gcs", "google/bigquery"],
            },
        )

    def test_name_falls_back_to_slug(self):
        record = build_site.collection_record(result("gcs"))
        self.assertEqual(
            record, {"name": "google", "summary": "", "members": ["google/gcs"]}
        )

    def test_single_entry_is_not_a_collection(self):
        self.assertIsNone(build_site.collection_record(result("", name="Google")))


def declared(text: str) -> tuple[dict, list[str]]:
    with tempfile.TemporaryDirectory() as root:
        (Path(root) / "skills.toml").write_text(text, encoding="utf-8")
        return collection_files.load("skills", Path(root))


class Declared(unittest.TestCase):
    def test_reads_a_collection(self):
        records, errors = declared(
            '[design]\nname = "Design"\nsummary = "Art."\nmembers = ["a", "b"]\n'
        )
        self.assertEqual(errors, [])
        self.assertEqual(
            records,
            {"design": {"name": "Design", "summary": "Art.", "members": ["a", "b"]}},
        )

    def test_no_file_is_no_collections(self):
        with tempfile.TemporaryDirectory() as root:
            self.assertEqual(collection_files.load("skills", Path(root)), ({}, []))

    def test_rejects_a_bad_table(self):
        records, errors = declared('[Design]\nmembers = []\nicon = "x"\n')
        self.assertEqual(records, {})
        self.assertEqual(len(errors), 4)  # slug, unknown key, name, members

    def test_rejects_a_member_twice(self):
        _, errors = declared('[d]\nname = "D"\nmembers = ["a", "a"]\n')
        self.assertIn("twice", errors[0])


MANIFESTS = {"google": {"name": "Google", "summary": "", "members": ["google/gcs"]}}


class Merge(unittest.TestCase):
    def merge(self, records: dict) -> tuple[dict, list[str]]:
        return collection_files.merge(
            "skills", records, MANIFESTS, {"a", "b", "google/gcs"}
        )

    def test_joins_both_sources(self):
        record = {"name": "D", "summary": "", "members": ["a"]}
        merged, errors = self.merge({"d": record})
        self.assertEqual(errors, [])
        self.assertEqual(merged, {**MANIFESTS, "d": record})

    def test_rejects_an_unknown_member(self):
        _, errors = self.merge({"d": {"name": "D", "summary": "", "members": ["z"]}})
        self.assertIn("no entry", errors[0])

    def test_rejects_a_member_of_a_manifest(self):
        _, errors = self.merge(
            {"d": {"name": "D", "summary": "", "members": ["google/gcs"]}}
        )
        self.assertIn("'google'", errors[0])

    def test_rejects_an_entry_in_two(self):
        one = {"name": "D", "summary": "", "members": ["a"]}
        _, errors = self.merge({"d": one, "e": {**one, "name": "E"}})
        self.assertIn("already in 'd'", errors[0])

    def test_rejects_a_manifest_slug(self):
        _, errors = self.merge(
            {"google": {"name": "G", "summary": "", "members": ["a"]}}
        )
        self.assertIn("already a collection", errors[0])


if __name__ == "__main__":
    unittest.main()
