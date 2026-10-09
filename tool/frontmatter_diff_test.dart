// The marketplace's validation is two tiers that must agree: the Dart CLI
// in a sibling entoli checkout (tool/validate_marketplace.dart — the source
// of truth) and the Python port (scripts/validate.py). This test builds one
// fixture tree, drives BOTH over it, and asserts each accepts and refuses
// what the marketplace promises, with the reason substring to match. It is
// the check that a marketplace CI green really means entoli accepts the
// entry, and that the quick local pass says the same thing.
//
// The entoli checkout is found at ../entoli, or wherever ENTOLI_CHECKOUT
// points.
//
//   dart tool/frontmatter_diff_test.dart
import "dart:io";

final repo = Directory.current.path;
final entoliRoot = Platform.environment["ENTOLI_CHECKOUT"] ?? "$repo/../entoli";
final cli = "$entoliRoot/tool/validate_marketplace.dart";

void main() {
  final cliFile = File(cli);
  if (!cliFile.existsSync()) {
    stderr.writeln(
        "no entoli checkout with tool/validate_marketplace.dart at $entoliRoot");
    exit(2);
  }

  // (slug, section, frontmatter, expected accept, reason substring when
  // refused). `name` in each fixture is the slug, which is the rule most
  // cases are built to test around.
  final cases = <(String, String, String Function(String), bool, String)>[
    (
      "plain-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\n---\n\nbody\n",
      true,
      ""
    ),
    (
      "folded-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: >-\n  folded description\n  over lines.\nmetadata:\n  author: A\n---\n",
      true,
      ""
    ),
    (
      "literal-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: |-\n  literal lines\n  stay.\nmetadata:\n  author: A\n  version: 1.0.0\n---\n",
      true,
      ""
    ),
    (
      "comments-skill",
      "skills",
      (slug) => "---\nname: $slug # the name\ndescription: quoted \"value\" here # and a comment\nmetadata:\n  author: 'sq' # noted\n---\n",
      true,
      ""
    ),
    (
      "prerelease-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\n  version: 2.0.0-rc.1+build\n  tags: a, b\n---\n",
      true,
      ""
    ),
    (
      "legacy-colon-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: audits the code: all of it\nmetadata:\n  author: A\n---\n",
      true,
      ""
    ),
    (
      "no-block-skill",
      "skills",
      (_) => "no frontmatter here\n",
      false,
      "no frontmatter block"
    ),
    (
      "no-name-skill",
      "skills",
      (slug) => "---\ndescription: d\nmetadata:\n  author: A\n---\n",
      false,
      "missing 'name'"
    ),
    (
      "name-mismatch-skill",
      "skills",
      (slug) => "---\nname: other\ndescription: d\nmetadata:\n  author: A\n---\n",
      false,
      "does not match the folder"
    ),
    (
      "unknown-key-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nauthor: A\n---\n",
      false,
      "unknown frontmatter key"
    ),
    (
      "bad-semver-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  version: 1.0\n  author: A\n---\n",
      false,
      "SemVer"
    ),
    (
      "list-tags-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\n  tags: [a, b]\n---\n",
      false,
      "comma-separated"
    ),
    (
      "dup-tags-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\n  tags: a, a\n---\n",
      false,
      "duplicates"
    ),
    (
      "no-author-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\n---\n",
      false,
      "author"
    ),
    (
      "metadata-last-skill",
      "skills",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\nother: x\n---\n",
      false,
      "unknown frontmatter key"
    ),
    (
      "plain-agent",
      "agents",
      (slug) => "---\ndescription: an agent for things.\nmetadata:\n  author: A\n---\n\nYou are an agent.\n",
      true,
      ""
    ),
    (
      "named-agent",
      "agents",
      (slug) => "---\nname: $slug\ndescription: d\nmetadata:\n  author: A\n---\n",
      false,
      "file name"
    ),
    (
      "no-desc-agent",
      "agents",
      (_) => "---\nmetadata:\n  author: A\n---\nbody",
      false,
      "no description"
    ),
    (
      "no-author-agent",
      "agents",
      (slug) => "---\ndescription: d\n---\nbody",
      false,
      "author"
    ),
  ];

  final tmp = Directory.systemTemp.createTempSync("fmcheck");
  for (final (slug, section, frontmatter, _, _) in cases) {
    final dir = Directory("${tmp.path}/$section/$slug")
      ..createSync(recursive: true);
    File("${dir.path}/${section == "skills" ? "SKILL.md" : "PROMPT.md"}")
        .writeAsStringSync(frontmatter(slug));
    File("${dir.path}/README.md").writeAsStringSync("# r\n");
  }
  for (final (runner, argv, name) in [
    (
      "dart",
      ["tool/validate_marketplace.dart", "--data-root", tmp.path],
      entoliRoot
    ),
    (
      "python",
      ["scripts/validate.py", "--data-root", tmp.path],
      repo
    ),
  ]) {
    validateTier(tmp, runner, argv, name, cases);
  }
  tmp.deleteSync(recursive: true);
}

/// Runs one validation tier over the fixture tree and asserts its outcomes.
void validateTier(
  Directory tmp,
  String runner,
  List<String> argv,
  String workDir,
  List<(String, String, String Function(String), bool, String)> cases,
) {
  final result = Process.runSync(
      runner == "dart" ? "dart" : "python3",
      runner == "dart" ? argv : argv,
      workingDirectory: workDir);
  final out = (result.stdout as String) + (result.stderr as String);
  // Problem lines are "  <data-root>/skills/<slug>/<file>: <message>"; an
  // entry can have several. The expected reason needs to be among them.
  final problemLine =
      RegExp(r"/(skills|agents)/([^/:]+)(?:/[^:]+)?: (.*)$", multiLine: true);
  final problems = <String, List<String>>{};
  for (final match in problemLine.allMatches(out)) {
    problems
        .putIfAbsent("${match.group(1)}/${match.group(2)}", () => [])
        .add(match.group(3)!);
  }

  final failures = <String>[];
  for (final (slug, section, _, wantAccept, wantReason) in cases) {
    final key = "$section/$slug";
    final reasons = problems[key];
    final refused = reasons != null;
    final ok =
        refused != wantAccept && (!refused || reasons!.any((r) => r.contains(wantReason)));
    if (!ok) {
      failures.add("$key: want accept=$wantAccept"
          "${wantAccept ? "" : " reason~'$wantReason'"}, got ${reasons ?? "accept"}");
    }
  }

  if (failures.isEmpty) {
    stdout.writeln(
        "$runner: ${cases.length} fixtures accept and refuse as the marketplace expects");
  } else {
    stderr.writeln("$runner tier disagrees:\n${failures.join("\n")}\n--- output ---\n$out");
    exit(1);
  }
}