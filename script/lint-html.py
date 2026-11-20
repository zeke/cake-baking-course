#!/usr/bin/env python3
"""Narrow authoring check, not an HTML sanitizer or Markdown renderer."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

# Required attributes and direct-child counts are the authoring contract.
REGISTRY = {
    'question': {'fieldset': ('data-course id', {'legend': (1, 1), 'p': (1, 1)}), 'legend': ('', {}), 'p': ('', {})},
    'quiz': {'fieldset': ('data-course id data-answer', {'legend': (1, 1), 'ol': (1, 1)}), 'legend': ('', {}), 'ol': ('', {'li': (2, 5)}), 'li': ('data-id data-feedback', {})},
    'matching': {'fieldset': ('data-course id', {'legend': (1, 1), 'dl': (1, 1)}), 'legend': ('', {}), 'dl': ('', {'dt': (2, 5), 'dd': (2, 5)}), 'dt': ('data-id data-match', {}), 'dd': ('data-id', {})},
    'teach-back': {'fieldset': ('data-course id', {'legend': (1, 1), 'p': (1, 1), 'ol': (1, 1)}), 'legend': ('', {}), 'p': ('', {}), 'ol': ('', {'li': (1, 5)}), 'li': ('', {})},
}

class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.roots, self.errors = [], [], []
    def error(self, line, message):
        self.errors.append((line, message))
    def handle_starttag(self, tag, attrs):
        if not self.stack and tag != 'fieldset':
            return
        node = {'tag': tag, 'attrs': dict(attrs), 'children': [], 'text': '', 'line': self.getpos()[0]}
        if len(attrs) != len(dict(attrs)):
            self.error(node['line'], 'duplicate attribute')
        if self.stack:
            self.stack[-1]['children'].append(node)
        else:
            self.roots.append(node)
        self.stack.append(node)
    def handle_endtag(self, tag):
        if not self.stack:
            return
        if self.stack[-1]['tag'] != tag:
            self.error(self.getpos()[0], f'unexpected closing </{tag}>')
        else:
            self.stack.pop()
    def handle_data(self, text):
        if self.stack:
            self.stack[-1]['text'] += text


def lint(source):
    # Ignore fenced examples and frontmatter while retaining source line numbers.
    lines = source.splitlines(keepends=True)
    fence = None
    frontmatter = bool(lines and lines[0].strip() == '---')
    for i, line in enumerate(lines):
        if frontmatter:
            lines[i] = '\n'
            if i and line.strip() == '---': frontmatter = False
            continue
        m = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence:
            lines[i] = '\n'
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*', line): fence = None
        elif m:
            fence = m[1]; lines[i] = '\n'
    parser = Blocks(); parser.feed(''.join(lines)); parser.close()
    for n in parser.stack: parser.error(n['line'], f'unclosed <{n["tag"]}>')
    ids = set()
    for root in parser.roots:
        kind = root['attrs'].get('data-course')
        if kind not in REGISTRY:
            parser.error(root['line'], f'unknown data-course {kind!r}'); continue
        schema = REGISTRY[kind]
        def check(n):
            if n['tag'] not in schema:
                parser.error(n['line'], f'unknown child <{n["tag"]}>'); return
            attrs, children = schema[n['tag']]; required = set(attrs.split())
            for a in sorted(set(n['attrs']) - required): parser.error(n['line'], f'unknown attribute {a}')
            for a in sorted(required):
                if not n['attrs'].get(a): parser.error(n['line'], f'missing attribute {a}')
            if children and n['text'].strip(): parser.error(n['line'], 'text must be in a child element')
            if not children and not n['text'].strip(): parser.error(n['line'], 'missing text')
            for tag, (lo, hi) in children.items():
                count = sum(c['tag'] == tag for c in n['children'])
                if not lo <= count <= hi: parser.error(n['line'], f'expected {lo}..{hi} <{tag}> children, got {count}')
            for c in n['children']:
                if c['tag'] not in children: parser.error(c['line'], f'<{c["tag"]}> not allowed in <{n["tag"]}>')
                check(c)
        check(root)
        rid = root['attrs'].get('id')
        if rid in ids: parser.error(root['line'], f'duplicate block id {rid}')
        ids.add(rid)
        items = [c for group in root['children'] for c in group['children']]
        item_ids = [n['attrs'].get('data-id') for n in items if 'data-id' in n['attrs']]
        if len(set(item_ids)) != len(item_ids): parser.error(root['line'], 'duplicate choice/pair id')
        if kind == 'quiz' and item_ids.count(root['attrs'].get('data-answer')) != 1:
            parser.error(root['line'], 'data-answer must reference exactly one choice')
        if kind == 'matching':
            targets = [n['attrs'].get('data-id') for n in items if n['tag'] == 'dd']
            matches = [n['attrs'].get('data-match') for n in items if n['tag'] == 'dt']
            if sorted(str(x) for x in targets) != sorted(str(x) for x in matches):
                parser.error(root['line'], 'data-match must pair each definition exactly once')
    return parser.errors

if __name__ == '__main__':
    paths = [Path(p) for p in sys.argv[1:]] or sorted((Path(__file__).resolve().parent.parent / 'exercises').glob('*.md'))
    errors = [(p, line, message) for p in paths for line, message in lint(p.read_text())]
    for p, line, message in errors: print(f'{p}:{line}: {message}')
    if not errors: print(f'HTML blocks valid in {len(paths)} files')
    sys.exit(bool(errors))
