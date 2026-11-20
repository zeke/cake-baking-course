#!/usr/bin/env python3
import importlib.util
import sys
from pathlib import Path
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('blocks', ROOT / 'script/lint-html.py')
blocks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blocks)

class AuthoringTests(unittest.TestCase):
    def test_valid_exercises(self):
        for file in (ROOT / 'exercises').glob('*.md'):
            self.assertEqual(blocks.lint(file.read_text()), [], str(file))
    def test_all_block_kinds_are_authored(self):
        kinds = []
        for file in sorted((ROOT / 'exercises').glob('*.md')):
            parser = blocks.Blocks()
            parser.feed(file.read_text())
            kinds.extend(node['attrs']['data-course'] for node in parser.roots)
        self.assertEqual(kinds.count('quiz'), 4)
        self.assertEqual(set(kinds), set(blocks.REGISTRY))
    def test_fixtures(self):
        for file in (ROOT / 'test/html-fixtures').glob('*.md'):
            with self.subTest(file=file.name):
                errors = blocks.lint(file.read_text())
                if file.name.startswith('valid'):
                    self.assertEqual(errors, [])
                else:
                    self.assertTrue(errors)
                    self.assertTrue(all(line > 0 for line, _ in errors))
    def test_required_diagnostics(self):
        for name, text in [('typo', 'unknown attribute'), ('missing-child', 'expected'), ('bad-answer', 'exactly one choice'), ('two-correct', 'duplicate attribute'), ('bad-pair', 'pair each definition')]:
            errors = blocks.lint((ROOT / f'test/html-fixtures/{name}.md').read_text())
            self.assertTrue(any(text in message for _, message in errors), errors)

unittest.main()
