// Re-export entoli's Frontmatter for the differential test so the library
// file's own package imports stay untouched. Requires a sibling entoli
// checkout: ../entoli relative to this repo's root.
export "../../entoli/lib/domain/frontmatter.dart" show Frontmatter;