#!/usr/bin/env python3
"""
validate_component.py — structural + consistency checks for component
context files (YAML frontmatter + Markdown body).

Usage:
    python3 validate_component.py path/to/component.md

Encodes every bug class caught during Button and Text Input extraction:
  - missing/malformed frontmatter (no closing '---', bad YAML)
  - indentation drift between sibling list items
  - enum values with no designTokens entry and no explanation
  - light/dark theme values that are suspiciously identical (possible
    duplication instead of independent verification)
  - needsReview entries that contradict what's actually in the frontmatter
  - missing required per-prop fields (category, default, etc)

Exit code 0 = no blocking issues (warnings may still exist, review them).
Exit code 1 = parse failure or blocking issue found.
"""
import sys
import re

try:
    import frontmatter
except ImportError:
    print("Missing dependency. Install with: pip install python-frontmatter")
    sys.exit(1)


REQUIRED_PROP_FIELDS = ["name", "type", "category", "required", "default", "values", "designTokens"]
VALID_CATEGORIES = {"visual", "content", "accessibility", "behavioral"}


def load(path):
    with open(path, "r") as f:
        raw = f.read()

    if not raw.startswith("---"):
        print(f"❌ PARSE FAILED: file does not start with '---' — no frontmatter delimiter found at all.")
        sys.exit(1)

    try:
        post = frontmatter.loads(raw)
    except Exception as e:
        print(f"❌ PARSE FAILED (YAML error):\n{e}")
        sys.exit(1)

    if not post.metadata:
        print("❌ PARSE FAILED: frontmatter block is empty or missing its closing '---'.")
        print("   (The file may look correct visually but has no closing delimiter,")
        print("    which means everything is being read as unstructured body text.)")
        sys.exit(1)

    return post


def check_indentation_hint(path):
    """Heuristic: look for '- name:' lines specifically within the props:
    block at inconsistent leading-space counts. Scoped to props only, not
    any '- name:' in the frontmatter, since nested lists (e.g.
    serviceApi.methods) legitimately sit at a different indent depth."""
    with open(path) as f:
        raw = f.read()

    parts = raw.split("---", 2)
    if len(parts) < 3:
        return None  # no closing delimiter; load() will already report this as a hard failure
    frontmatter_block = parts[1]

    lines = frontmatter_block.splitlines()
    indents = []
    in_props_block = False
    props_block_indent = None
    for line in lines:
        stripped = line.strip()
        if not in_props_block:
            if stripped == "props:":
                in_props_block = True
            continue
        # We're inside the props: block. A line that is a new top-level
        # frontmatter key (no leading whitespace, ends with ':') ends it.
        if line and not line[0].isspace() and stripped.endswith(":"):
            break
        m = re.match(r"^( *)- name:", line)
        if m:
            indents.append(len(m.group(1)))

    if indents and len(set(indents)) > 1:
        return f"Inconsistent indentation found across '- name:' entries within props: (seen indent levels {sorted(set(indents))}, should all match)"
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 validate_component.py path/to/component.md")
        sys.exit(1)

    path = sys.argv[1]
    issues = []
    warnings = []

    # Raw indentation heuristic runs even if YAML parsing would fail,
    # so it's checked first for a more useful error message.
    indent_issue = check_indentation_hint(path)
    if indent_issue:
        issues.append(indent_issue)

    post = load(path)
    meta = post.metadata
    body = post.content

    props = meta.get("props", [])
    print(f"✅ Parses cleanly. {len(props)} props found.\n")

    # --- relatedComponents structural check ---
    related = meta.get("relatedComponents")
    if related:
        for r in related:
            if not isinstance(r, dict):
                issues.append(f"relatedComponents entry is not a structured object: {r}")
                continue
            for field in ["name", "relationship", "whenToUse"]:
                if field not in r:
                    issues.append(f"[relatedComponents: {r.get('name','?')}] missing required field: {field}")
            if r.get("relationship") not in {"container", "child", "alternative"}:
                warnings.append(
                    f"[relatedComponents: {r.get('name','?')}] relationship "
                    f"'{r.get('relationship')}' is not one of container/child/alternative"
                )
        if "## Related Components" not in body:
            warnings.append(
                "'relatedComponents' is populated in frontmatter but no "
                "'## Related Components' section found in body"
            )

    # --- apiTypes consistency checks ---
    api_types = meta.get("apiTypes")
    if api_types is None:
        warnings.append(
            "No 'apiTypes' field found — assuming element-only for legacy "
            "compatibility. If this component has a service API, add "
            "apiTypes explicitly."
        )
        api_types = ["element"]
    else:
        if not isinstance(api_types, list) or not api_types:
            issues.append(f"apiTypes should be a non-empty list, got: {api_types}")
        if "element" not in api_types and props:
            issues.append(
                "'element' is not in apiTypes, but props are populated — "
                "props/events/designTokens should be omitted entirely for "
                "service-only components."
            )
        if "service" in api_types:
            service_api = meta.get("serviceApi")
            if not service_api:
                issues.append(
                    "'service' is in apiTypes but no 'serviceApi' field was found in frontmatter."
                )
            elif not service_api.get("methods"):
                issues.append("serviceApi has no methods listed.")
            if "## Service API" not in body:
                issues.append("'service' is in apiTypes but no '## Service API' section found in body.")
        if "element" in api_types and "service" in api_types:
            if "## When to use which approach" not in body:
                warnings.append(
                    "Component has both element and service APIs but no "
                    "'## When to use which approach' section found in body — "
                    "this is the most important section for a dual-API component."
                )

    # --- structural completeness ---
    names_seen = []
    for p in props:
        name = p.get("name", "<unnamed>")
        names_seen.append(name)
        for field in REQUIRED_PROP_FIELDS:
            if field not in p:
                issues.append(f"[{name}] missing required field: {field}")
        if p.get("category") not in VALID_CATEGORIES:
            issues.append(f"[{name}] category '{p.get('category')}' is not one of {VALID_CATEGORIES}")
        if p.get("default") is None:
            warnings.append(f"[{name}] default is null/empty — should be an explicit value or the string 'none found'")

    dupes = {n for n in names_seen if names_seen.count(n) > 1}
    if dupes:
        issues.append(f"Duplicate prop names: {dupes}")

    # --- enum coverage vs designTokens ---
    for p in props:
        name = p.get("name")
        values = p.get("values") or []
        tokens = p.get("designTokens") or {}
        if values and tokens:
            missing = [v for v in values if v not in tokens]
            if missing:
                warnings.append(
                    f"[{name}] enum values with no designTokens entry: {missing} "
                    f"— confirm this is intentionally named in needsReview, not an oversight"
                )

    # --- light/dark duplication heuristic ---
    for p in props:
        name = p.get("name")
        tokens = p.get("designTokens") or {}
        for val, data in tokens.items():
            if isinstance(data, dict) and "light" in data and "dark" in data:
                lr = data["light"].get("resolvesTo")
                dr = data["dark"].get("resolvesTo")
                if lr == dr:
                    warnings.append(
                        f"[{name}={val}] light and dark resolvesTo are IDENTICAL ({lr}) — "
                        f"verify this was independently traced from a real dark-theme token, "
                        f"not duplicated from light"
                    )

    # --- events structure check ---
    events = meta.get("events", [])
    required_event_fields = ["name", "payloadType", "firesWhen", "detailAccess", "bindingSyntax"]
    for e in events:
        if not isinstance(e, dict):
            issues.append(f"events entry is not a structured object: {e}")
            continue
        for field in required_event_fields:
            if field not in e:
                issues.append(f"[event: {e.get('name','?')}] missing required field: {field}")
        payload = e.get("payloadType", "")
        if payload and not payload.strip().startswith("CustomEvent"):
            warnings.append(
                f"[event: {e.get('name','?')}] payloadType '{payload}' does not start with "
                f"'CustomEvent<...>' — since this library exposes web components, event payloads "
                f"should almost always be wrapped in CustomEvent. Verify this isn't a plain "
                f"Angular-only payload type that won't match runtime behavior."
            )

    # --- .detail access mentioned in body's Events section, for non-void events ---
    events_section_match = re.search(r"## Events(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if events and events_section_match:
        events_body = events_section_match.group(1)
        for e in events:
            if not isinstance(e, dict):
                continue
            name = e.get("name", "")
            payload = e.get("payloadType", "")
            if "void" not in payload.lower() and name:
                # crude check: does the events body mention .detail near this event's name
                idx = events_body.find(f"### {name}")
                if idx == -1:
                    idx = events_body.find(name)
                nearby = events_body[idx:idx+1200] if idx != -1 else ""
                if idx != -1 and ".detail" not in nearby:
                    warnings.append(
                        f"[event: {name}] has a non-void payload but no '.detail' access shown "
                        f"nearby in the Events body section — confirm a real handler snippet "
                        f"demonstrating .detail access is actually present"
                    )
    elif events and not events_section_match:
        warnings.append("'events' entries exist in frontmatter but no '## Events' section found in body")

    # --- heuristic: events mentioned in prose but not in structured events list ---
    event_name_pattern = re.compile(r"\b(\w+Change|\w+Click|\w+Focus|\w+Blur|\w+Submit)\b")
    documented_event_names = {e.get("name") for e in events if isinstance(e, dict)}
    prose_blob = body + " ".join(meta.get("propInteractions", []))
    mentioned = set(event_name_pattern.findall(prose_blob))
    # filter out obvious non-events (prop names that happen to match the pattern)
    prop_names_set = set(names_seen)
    likely_undocumented_events = {m for m in mentioned if m not in documented_event_names and m not in prop_names_set}
    if likely_undocumented_events:
        warnings.append(
            f"Possible event names mentioned in prose but NOT in the structured 'events' list: "
            f"{likely_undocumented_events} — verify these aren't real @Output()s that got left "
            f"as a passing mention instead of a full events entry"
        )

    if not events:
        warnings.append(
            "'events' list is empty or missing entirely — confirm this component genuinely has "
            "no @Output()s, rather than them simply not having been traced yet"
        )

    # --- jointTokens sanity: should represent 2+ prop combinations, not single-prop data ---
    joint = meta.get("jointTokens", [])
    for jt in joint:
        combo = jt.get("combination", "")
        if "," not in combo:
            warnings.append(
                f"jointTokens entry '{combo}' only references one prop — jointTokens should "
                f"only be used for combinations of 2+ props; single-prop data belongs in that "
                f"prop's own designTokens instead"
            )

    # --- needsReview / propInteractions item-type check (catches unquoted
    # strings containing 'key: value' patterns getting parsed as dicts) ---
    for list_name in ["needsReview", "propInteractions"]:
        items = meta.get(list_name, [])
        for i, item in enumerate(items):
            if not isinstance(item, str):
                issues.append(
                    f"{list_name}[{i}] did not parse as a plain string (got {type(item).__name__}: "
                    f"{str(item)[:80]}...) — this usually means the source text had an unquoted "
                    f"colon-space ('key: value') that YAML misread as a nested mapping. "
                    f"Fix by wrapping that entry in double quotes."
                )

    # --- needsReview contradiction check (heuristic) ---
    needs_review = [n for n in meta.get("needsReview", []) if isinstance(n, str)]
    review_blob = " ".join(needs_review).lower()
    for p in props:
        name = p.get("name")
        tokens = p.get("designTokens") or {}
        has_dark_data = any(isinstance(d, dict) and "dark" in d for d in tokens.values())
        if has_dark_data and "dark theme" in review_blob and name.lower() in review_blob:
            warnings.append(
                f"[{name}] has populated 'dark' theme data AND is referenced near 'dark theme' "
                f"in needsReview — double check these aren't contradicting each other"
            )

    # --- examples sanity: should be in body as fenced code, not in frontmatter ---
    if "examples" in meta:
        issues.append("'examples' found in frontmatter — examples must be in the Markdown body as fenced code blocks, not YAML")

    # --- body sanity ---
    prop_names_with_sections = set(re.findall(r"^## (\S+)", body, re.MULTILINE))
    missing_sections = [n for n in names_seen if n not in prop_names_with_sections]
    if missing_sections:
        warnings.append(f"Props with no '## <name>' section found in body: {missing_sections}")

    if "## Examples" not in body and "##Examples" not in body:
        warnings.append("No '## Examples' section found in body")

    if "```" not in body:
        warnings.append("No fenced code blocks found in body — examples may be missing or malformed")

    # --- report ---
    print("== Issues (blocking) ==")
    if not issues:
        print("  None")
    for i in issues:
        print(f"  ❌ {i}")

    print("\n== Warnings (review, not necessarily wrong) ==")
    if not warnings:
        print("  None")
    for w in warnings:
        print(f"  ⚠️  {w}")

    print(f"\nneedsReview entries: {len(meta.get('needsReview', []))}")
    print(f"jointTokens entries: {len(joint)}")

    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()