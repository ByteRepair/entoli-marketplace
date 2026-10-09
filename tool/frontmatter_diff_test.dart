// The marketplace's validation is the Dart CLI in a sibling entoli
// checkout (tool/validate_marketplace.dart); this test drives it with the
// canonical frontmatter fixtures and asserts the outcomes entoli produces —
// accepted or refused, with a reason substring to match. It is the check
// that a marketplace CI green really does mean entoli accepts the entry.
//
// The entoli checkout is found at ../entoli, or wherever ENOLI_CHECKOUT
// points.
//
//   dart tool/frontmatter_diff_test.dart
import "dart:io";

final repo = Directory.current.path;
final entoliRoot = Platform.environment["ENTOLI_CHECKOUT"] ?? "$repo/../entoli";
final cli = "$entoliRoot/tool/validate_marketplace.dart";

void main() {
  final entoliDir = Directory(entoliRoot);
  final cliFile = File(cli);
  if (!entoliDir.existsSync() || !cliFile.existsSync()) {
    stderr.writeln("no entoli checkout with tool/validate_marketplace.dart at $entoliRoot");
    exit(2);
  }

  // (frontmatter source, expected accept, reason substring when refused)
  final cases = <(String, bool, String)>[
    ("---\nname: s\ndescription: d\nmetadata:\n  author: A\n---\n\nbody\n", true, ""),
    ("---\nname: s\ndescription: >-\n  folded description\n  over lines.\nmetadata:\n  author: A\n---\n", true, ""),
    ("---\nname: s\ndescription: |-\n  literal lines\n  stay.\nmetadata:\n  author: A\n  version: 1.0.0\n---\n", true, ""),
    ("---\nname: s\ndescription: quoted \"value\" here # and a comment\nmetadata:\n  author: 'sq'\n---\n", true, ""),
    ("---\nname: s\ndescription: d\nmetadata:\n  author: A\n  version: 2.0.0-rc.1+build\n  tags: a, b\n---\n", true, ""),
    // refusals
    ("no frontmatter here\n", false, "no frontmatter block"),
    ("---\ndescription: d\nmetadata:\n  author: A\n---\n", false, "missing 'name'"),
    ("---\nname: other\ndescription: d\nmetadata:\n  author: A\n---\n", false, "does not match the folder"),
    ("---\nname: s\ndescription: d\nauthor: A\n---\n", false, "unknown frontmatter key"),
    ("---\nname: s\ndescription: d\nmetadata:\n  version: 1.0\n  author: A\n---\n", false, "SemVer"),
    ("---\nname: s\ndescription: d\nmetadata:\n  author: A\n  tags: [a, b]\n---\n", false, "comma-separated"),
    ("---\nname: s\ndescription: d\nmetadata:\n  author: A\n  tags: a, a\n---\n", false, "duplicates"),
    ("---\nname: s\ndescription: d\n---\n", false, "no usable 'author'"),
    ("---\nname: s\ndescription: d\nmetadata:\n  author: A\nother: x\n---\n", false, "unknown frontmatter key"),
    // legacy shapes entoli still accepts: not YAML, parsed by the fallback
    ("---\nname: s\ndescription: audits the code: all of it\nmetadata:\n  author: A\n---\n", true, ""),
  ];

  var failures = 0;
  final tmp = Directory.systemTemp.createTempSync("fmcheck");
  for (final (frontmatter, wantAccept, wantReason) in cases) {
    final skillDir = Directory("${tmp.path}/skills/s")
      ..createSync(recursive: true);
    File("${skillDir.path}/SKILL.md").writeAsStringSync(frontmatter);
    File("${skillDir.path}/README.md").writeAsStringSync("# r\n");
    final result = Process.runSync("dart", [
      "run",
      "tool/validate_marketplace.dart",
      "--data-root",
      tmp.path,
    ], workingDirectory: entoliRoot);
    final out = (result.stdout as String) + (result.stderr as String);
    final accepted = result.exitCode == 0;
    final ok = accepted == wantAccept &&
        (wantAccept || out.contains(wantReason)) &&
        (accepted || wantAccept || out.contains(wantReason));
    if (!ok) {
      failures++;
      stderr.writeln("MISMATCH on ${frontmatter.replaceAll("\n", "\\n")}\n"
          "  want accept=$wantAccept reason='$wantReason'\n"
          "  got exit=${result.exitCode}\n$out");
    }
    skillDir.deleteSync(recursive: true);
  }
  tmp.deleteSync(recursive: true);
  if (failures == 0) {
    stdout.writeln("${cases.length} cases: entoli accepts and refuses as the marketplace expects");
  } else {
    stderr.writeln("$failures mismatch(es)");
    exit(1);
  }
}