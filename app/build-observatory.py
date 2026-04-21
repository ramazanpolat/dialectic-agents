#!/usr/bin/env python3
"""
build-observatory.py
Generates dialectic-observatory-v2.html from local artifact .md files.

Usage:
    python3 build-observatory.py

Output:
    dialectic-observatory-v2.html   (new file, never overwrites original)
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).parent
AGENTS_DIR = BASE / "dialectic-agents"
TEMPLATE = BASE / "dialectic-observatory-20260222-1519.html"
OUTPUT = BASE / "dialectic-observatory-v2.html"

# Agent metadata — updated when new agents join or roles change
AGENTS = {
    'logos':     {'name': 'Logos',     'color': '#00b894', 'layers': '0-1',   'role': 'Definitions & Primitives'},
    'axiom':     {'name': 'Axiom',     'color': '#6c5ce7', 'layers': '2',     'role': 'Axioms & Postulates'},
    'propo':     {'name': 'Propo',     'color': '#fdcb6e', 'layers': '3-4',   'role': 'Propositions & Premises'},
    'ori':       {'name': 'Ori',       'color': '#e17055', 'layers': '—',     'role': 'A Priori / A Posteriori Classifier'},
    'tribunal':  {'name': 'Tribunal',  'color': '#0984e3', 'layers': '5-8',   'role': 'Inference & Theorems'},
    'hypothex':  {'name': 'Hypothex',  'color': '#d63031', 'layers': '9',     'role': 'Hypotheses'},
    'theorica':  {'name': 'Theorica',  'color': '#e84393', 'layers': '10-11', 'role': 'Theories & Models'},
    'synthesis': {'name': 'Synthesis', 'color': '#00cec9', 'layers': '—',     'role': 'Dialectical Integration'},
    'watcher':   {'name': 'Watcher',   'color': '#636e72', 'layers': '—',     'role': 'Observer & Orchestrator'},
}

# Canonical agent order for display
AGENT_ORDER = list(AGENTS.keys())

# Prefixes to strip from H1 titles when extracting short title
TITLE_PREFIXES = re.compile(
    r'^(?:'
    r'Definition:\s+|'
    r'Primitive:\s+|'
    r'Axiom:\s+|'
    r'Postulate:\s+|'
    r'Proposition:\s+|'
    r'Theorem:\s+|'
    r'Lemma:\s+|'
    r'Corollary:\s+|'
    r'Hypothesis:\s+|'
    r'Theory:\s+|'
    r'Model:\s+|'
    r'Synthesis:\s+|'
    r'Classification of [A-Z]+-\d+:\s+|'
    r'Classification:\s+'
    r')',
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Frontmatter parser (stdlib only — no PyYAML dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """
    Extract YAML frontmatter between --- delimiters.
    Returns (dict, body_text). Returns (None, text) if no frontmatter found.
    """
    m = re.match(r'^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n', text, re.DOTALL)
    if not m:
        return None, text

    fm_text = m.group(1)
    body = text[m.end():]
    data = {}

    for line in fm_text.split('\n'):
        line = line.rstrip('\r')
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            continue

        key, _, val = line.partition(':')
        key = key.strip()
        val = val.strip()

        if not key:
            continue

        # Quoted string (single or double)
        if (val.startswith('"') and val.endswith('"')) or \
           (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]

        # Inline YAML list [A, B, C] or ["A", "B"] or []
        elif val.startswith('[') and val.endswith(']'):
            inner = val[1:-1].strip()
            if not inner:
                val = []
            else:
                items = [
                    item.strip().strip('"').strip("'")
                    for item in inner.split(',')
                ]
                val = [i for i in items if i]

        # Numeric
        elif re.match(r'^-?\d+(\.\d+)?$', val):
            try:
                val = float(val) if '.' in val else int(val)
            except ValueError:
                pass

        data[key] = val

    return data, body


def normalize_date(raw):
    """Ensure date string includes time component (append T00:00:00Z if needed)."""
    if not isinstance(raw, str) or not raw:
        return '2026-02-22T00:00:00Z'
    raw = raw.strip()
    if 'T' not in raw:
        return raw + 'T00:00:00Z'
    return raw


# ---------------------------------------------------------------------------
# Title & description extraction
# ---------------------------------------------------------------------------

def extract_title(body):
    """
    Pull H1 text from body, strip known type prefixes, strip leading 'The '.
    Returns empty string if no H1 found.
    """
    m = re.search(r'^#[ \t]+(.+)$', body, re.MULTILINE)
    if not m:
        return ''

    title = m.group(1).strip()
    title = TITLE_PREFIXES.sub('', title)

    # Strip leading "The "
    title = re.sub(r'^The\s+', '', title)

    # Normalize em-dash
    title = title.replace(' -- ', ' — ').replace('--', '—')

    return title[:80].strip()


def extract_desc(body):
    """
    Extract first paragraph from the most informative heading section.
    Tries headings in priority order, falls back to text after H1.
    Returns empty string if nothing useful found.
    """
    # Try headings in priority order
    heading_patterns = [
        r'##[ \t]+Statement',
        r'##[ \t]+Executive Summary',
        r'##[ \t]+Dialectical Synthesis',
        r'##[ \t]+Hypothesis Structure',
        r'##[ \t]+Theory Structure',
        r'##[ \t]+Summary',
        r'##[ \t]+Overview',
        r'##[ \t]+Abstract',
    ]

    section = ''
    for pat in heading_patterns:
        m = re.search(pat + r'[ \t]*\r?\n(.*?)(?=\n##[ \t]|\Z)', body, re.DOTALL)
        if m and m.group(1).strip():
            section = m.group(1)
            break

    if not section.strip():
        # Final fallback: text between H1 and next heading
        m2 = re.search(r'^#[ \t]+.+$\n(.*?)(?=\n#+|\Z)', body, re.DOTALL | re.MULTILINE)
        section = m2.group(1) if m2 else ''

    if not section.strip():
        return ''

    # Take first non-empty paragraph; prefer prose over list items
    paragraphs = re.split(r'\n\n+', section.strip())
    text = ''
    list_fallback = ''
    for p in paragraphs:
        p = p.strip()
        if not p or p.startswith('#') or p.startswith('|'):
            continue
        if re.match(r'^[-*] ', p):
            # Keep as fallback — strip list marker and any sub-items, take first line
            if not list_fallback:
                first_line = p.split('\n')[0]
                list_fallback = re.sub(r'^[-*]\s+', '', first_line)
        else:
            text = p
            break

    if not text:
        text = list_fallback

    if not text:
        return ''

    # Strip markdown formatting
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text[:400]


# ---------------------------------------------------------------------------
# Artifact parsing
# ---------------------------------------------------------------------------

def parse_artifact(path):
    """
    Parse a single artifact .md file.
    Returns a dict suitable for inclusion in the ARTIFACTS array, or None on error.
    """
    try:
        text = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  WARNING: Cannot read {path.name}: {e}", file=sys.stderr)
        return None

    fm, body = parse_frontmatter(text)
    if fm is None:
        print(f"  WARNING: No frontmatter in {path.name}", file=sys.stderr)
        return None

    artifact_id = str(fm.get('id', '')).strip()
    if not artifact_id:
        print(f"  WARNING: No id field in {path.name}", file=sys.stderr)
        return None

    agent = str(fm.get('agent', path.parent.parent.name)).strip().lower()
    artifact_type = str(fm.get('type', 'unknown')).strip()
    status = str(fm.get('status', 'draft')).strip()
    domain = str(fm.get('domain', 'unknown')).strip()
    created = normalize_date(fm.get('created'))

    depends_on = fm.get('depends_on', [])
    if not isinstance(depends_on, list):
        depends_on = []

    raw_conf = fm.get('confidence', 0.8)
    try:
        confidence = round(float(raw_conf), 4)
    except (TypeError, ValueError):
        confidence = 0.8

    raw_layer = fm.get('layer', 0)
    try:
        layer = int(raw_layer)
    except (TypeError, ValueError):
        layer = 0

    title = extract_title(body)
    desc = extract_desc(body)

    return {
        'id': artifact_id,
        'agent': agent,
        'type': artifact_type,
        'status': status,
        'title': title,
        'domain': domain,
        'depends': depends_on,
        'confidence': confidence,
        'layer': layer,
        'created': created,
        'desc': desc,
    }


# ---------------------------------------------------------------------------
# JavaScript generation
# ---------------------------------------------------------------------------

def js_str(s):
    """Encode a Python string as a JavaScript string literal (double-quoted JSON)."""
    return json.dumps(str(s), ensure_ascii=False)


def build_agents_js():
    """Generate the const AGENTS = {...}; block."""
    lines = ['const AGENTS = {']
    for key, ag in AGENTS.items():
        lines.append(
            f"  {key}:     {{ name: {js_str(ag['name'])}, "
            f"color: {js_str(ag['color'])}, "
            f"layers: {js_str(ag['layers'])}, "
            f"role: {js_str(ag['role'])} }},"
        )
    lines.append('};')
    return '\n'.join(lines)


def build_artifacts_js(artifacts):
    """Generate the const ARTIFACTS = [...]; block."""
    lines = ['const ARTIFACTS = [']

    current_agent = None
    for a in artifacts:
        if a['agent'] != current_agent:
            current_agent = a['agent']
            lines.append(f'  // {current_agent.upper()}')

        parts = [
            f"id:{js_str(a['id'])}",
            f"agent:{js_str(a['agent'])}",
            f"type:{js_str(a['type'])}",
            f"status:{js_str(a['status'])}",
            f"title:{js_str(a['title'])}",
            f"domain:{js_str(a['domain'])}",
            f"depends:{json.dumps(a['depends'], ensure_ascii=False)}",
            f"confidence:{a['confidence']}",
            f"layer:{a['layer']}",
            f"created:{js_str(a['created'])}",
            f"desc:{js_str(a['desc'])}",
        ]
        lines.append('  { ' + ', '.join(parts) + ' },')

    lines.append('];')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# HTML patching
# ---------------------------------------------------------------------------

def replace_block(html, start_marker, end_marker, replacement):
    """
    Replace the text from start_marker to end_marker (inclusive) with replacement.
    Raises ValueError if markers are not found.
    """
    start = html.find(start_marker)
    if start == -1:
        raise ValueError(f"Start marker not found: {start_marker!r}")

    end = html.find(end_marker, start)
    if end == -1:
        raise ValueError(f"End marker not found: {end_marker!r}")

    end += len(end_marker)
    return html[:start] + replacement + html[end:]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Verify inputs
    if not TEMPLATE.exists():
        print(f"ERROR: Template not found: {TEMPLATE}", file=sys.stderr)
        sys.exit(1)

    if not AGENTS_DIR.exists():
        print(f"ERROR: Agents directory not found: {AGENTS_DIR}", file=sys.stderr)
        sys.exit(1)

    # Load template
    template_html = TEMPLATE.read_text(encoding='utf-8')

    # Discover artifact files
    artifact_files = sorted(AGENTS_DIR.glob('*/artifacts/*.md'))
    print(f"Found {len(artifact_files)} artifact files in {AGENTS_DIR.name}/")

    # Parse
    artifacts = []
    skipped = 0
    for path in artifact_files:
        a = parse_artifact(path)
        if a:
            artifacts.append(a)
        else:
            skipped += 1

    if skipped:
        print(f"Skipped {skipped} file(s) with parse errors")

    # Sort: by canonical agent order, then by artifact ID
    def sort_key(a):
        try:
            idx = AGENT_ORDER.index(a['agent'])
        except ValueError:
            idx = len(AGENT_ORDER)
        return (idx, a['id'])

    artifacts.sort(key=sort_key)

    # Print per-agent summary
    counts = Counter(a['agent'] for a in artifacts)
    print(f"\nArtifacts by agent ({len(artifacts)} total):")
    for agent in AGENT_ORDER:
        if agent in counts:
            print(f"  {agent:12s}: {counts[agent]}")
    unknown = {k: v for k, v in counts.items() if k not in AGENT_ORDER}
    for agent, count in sorted(unknown.items()):
        print(f"  {agent:12s}: {count}  [unknown agent]")

    # Build replacement JS blocks
    agents_js = build_agents_js()
    artifacts_js = build_artifacts_js(artifacts)

    # Patch the template HTML
    try:
        html = replace_block(template_html, 'const AGENTS = {', '\n};', agents_js)
    except ValueError as e:
        print(f"ERROR patching AGENTS block: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        html = replace_block(html, 'const ARTIFACTS = [', '\n];', artifacts_js)
    except ValueError as e:
        print(f"ERROR patching ARTIFACTS block: {e}", file=sys.stderr)
        sys.exit(1)

    # Fix timeAgo() to use real current time instead of hardcoded date
    old_now = "const now = new Date('2026-02-22T18:00:00Z');"
    new_now = "const now = new Date();"
    if old_now in html:
        html = html.replace(old_now, new_now)
        print("\nFixed timeAgo() to use real current time")
    else:
        print("\nWARNING: Could not find hardcoded date in timeAgo() — skipped fix")

    # Write output (never touches the original)
    OUTPUT.write_text(html, encoding='utf-8')
    print(f"\nWrote: {OUTPUT.name}")
    print(f"Size:  {OUTPUT.stat().st_size:,} bytes")
    print(f"\nOpen in browser:")
    print(f"  open {OUTPUT}")


if __name__ == '__main__':
    main()
