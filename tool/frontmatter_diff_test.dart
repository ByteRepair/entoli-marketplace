// Differential test: entoli's Frontmatter.parse (Dart, via fm_dart.dart)
// against the Python port in scripts/validate.py, over adversarial
// frontmatter cases. Requires a sibling entoli checkout (../entoli).
//
//   dart tool/frontmatter_diff_test.dart
//
// Exits 0 when every case agrees on scalars, metadata, and block presence;
// prints divergences and exits 1 otherwise.
import "dart:convert";
import "dart:io";

import "fm_dart.dart";

void main() {
  final repo = Directory.current.path;
  final entoliFrontmatter = File("$repo/../entoli/lib/domain/frontmatter.dart");
  if (!entoliFrontmatter.existsSync()) {
    stderr.writeln("no entoli checkout at ${entoliFrontmatter.path}");
    exit(2);
  }

  final cases = <String>[
    "---\nname: foo\ndescription: bar\n---\n\nbody\n",
    "---\nname: \"quoted\"\ndescription: 'single'\n---\nbody\n",
    "---\nname: foo\nmetadata:\n  author: A\n  version: 1.2.0\n---\nbody\n",
    "---\nmetadata:\n  tags: a, b\n  author: X\n---\n",
    "---\n---\nbody\n",
    "---\ndescription: spaced   \nname:    indented-name\n---\n",
    "no block at all\n",
    "---\nunclosed\n",
    "\n---\nnot at start\n---\n",
    "---\r\nname: crlf\r\ndescription: crlf\r\n---\r\nbody\r\n",
    "---\nname: pre\nmetadata:\n  author: A\nother: after-block\n---\nbody\n",
    "---\nmetadata:\n  author: A\nname: after\n---\n",
    "---\nmetadata:\n  deeper:\n    x: 1\n  author: B\n---\n",
    "---\nmetadata:\n    author: four-space\n---\n",
    "---\nmetadata:\n  author: A\n    version: deeper\n---\n",
    "---\nmetadata:\n\n  author: after-blank\n---\n",
    "---\nmetadata: inline\n---\n",
    "---\nname: 'sq'\ndescription: \"dq\"\nmetadata:\n  author: 'q'\n  version: \"09.9.9\"\n---\n",
    "---\nname: a\"b\ndescription: it's\n---\n",
    "---\nname: \"\n---\n",
    "---\nname: \"unterminated\n---\n",
    "---\nname: a: b\ndescription: c: d\n---\n",
    "---\nurl: http://example.com\n---\n",
    "---\nname: spaced  value\n---\n",
    "---\nname: name\nname: second\n---\n",
    "---\nname-with-dash: v\nkey.name: v\nkey_name: v\nkey123: v\n---\n",
    "---\n NAME: upper \n---\n",
    "---\nname: v\n\ttabbed: x\n---\n",
    "---\nname: v\n metadata:\n   author: A\n---\n",
    "---\nlist:\n  - item\nname: keep\n---\n",
    "---\nmetadata:\n  author: A\n  tags: x,y,,z\n---\n",
    "---\nmetadatas: x\n---\n",
    "---\nmetadata2:\n  author: B\n---\n",
    "---\nname: empty-metadata\nmetadata:\n---\n",
    "---\nname: dup\nmetadata:\n  author: A\nmetadata:\n  author: B\n---\n",
    "---\ndescription: line1\n  continued: indented\n---\n",
  ];

  var divergences = 0;
  final tmp = Directory.systemTemp.createTempSync("fmtest");
  for (final source in cases) {
    final fm = Frontmatter.parse(source);
    final caseFile = File("${tmp.path}/case.txt");
    caseFile.writeAsStringSync(source);
    final result = Process.runSync("python3", [
      "-c",
      "import sys, json; sys.path.insert(0, r'$repo/scripts');"
          "import validate; s, m, b = validate.parse_frontmatter(open(sys.argv[1]).read());"
          "print(json.dumps({'scalars': s, 'metadata': m, 'has_block': b}))",
      caseFile.path,
    ]);
    if (result.exitCode != 0) {
      divergences++;
      stderr.writeln("python failed on ${jsonEncode(source)}:\n${result.stderr}");
      continue;
    }
    final py = jsonDecode(result.stdout as String) as Map<String, dynamic>;
    final pyScalars = (py["scalars"] as Map).cast<String, String>();
    final pyMeta = (py["metadata"] as Map).cast<String, String>();
    // Dart's block rule after its own CRLF normalization: --- opener AND a
    // closing \n--- — the same thing has_block reports on the Python side.
    final normalized = source.replaceAll("\r\n", "\n");
    final dartHasBlock =
        normalized.startsWith("---\n") && normalized.indexOf("\n---", 3) >= 0;
    final same = _eq(fm.scalars, pyScalars) &&
        _eq(fm.metadata, pyMeta) &&
        (py["has_block"] as bool) == dartHasBlock;
    if (!same) {
      divergences++;
      stderr.writeln("DIVERGENCE on: ${jsonEncode(source)}\n"
          "  dart scalars=${fm.scalars} metadata=${fm.metadata}\n"
          "  py   scalars=$pyScalars metadata=$pyMeta "
          "has_block=${py["has_block"]}");
    }
  }
  tmp.deleteSync(recursive: true);
  if (divergences == 0) {
    stdout.writeln("${cases.length} cases: dart and python parsers agree");
  } else {
    stderr.writeln("$divergences divergence(s)");
    exit(1);
  }
}

bool _eq(Map<String, String> a, Map<String, String> b) =>
    a.length == b.length && a.entries.every((e) => b[e.key] == e.value);