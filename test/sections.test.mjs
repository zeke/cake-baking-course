import { readFileSync, readdirSync, existsSync } from 'node:fs';
import assert from 'node:assert/strict';
import { test } from 'node:test';

const authored = JSON.parse(readFileSync(new URL('../resources/sections.json', import.meta.url)));
const exercises = readdirSync(new URL('../exercises/', import.meta.url)).filter(file => file.endsWith('.md')).sort();

test('every explicit section ends in its authored, unscored leading question', () => {
  assert.equal(exercises.length, 6);
  for (const file of exercises) {
    const slug = file.replace(/^\d+-/, '').replace(/\.md$/, '');
    const markdown = readFileSync(new URL(`../exercises/${file}`, import.meta.url), 'utf8');
    const body = markdown.replace(/^---\n[\s\S]*?\n---\n/, '');
    const sections = body.split(/\n---\n/);
    assert.equal(sections.length, 2);
    assert.equal((body.match(/^# /gm) ?? []).length, 1);
    const ids = new Set();
    for (const [index, section] of sections.entries()) {
      const data = authored.exercises[slug][index];
      assert.match(data.id, /^[a-z0-9]+(?:-[a-z0-9]+)*$/);
      assert.ok(!ids.has(data.id));
      ids.add(data.id);
      assert.ok(section.trim().endsWith(`Continue the conversation: ${data.question}`));
      assert.ok(data.question.endsWith('?'));
      assert.ok(data.responses.length >= 2);
      assert.ok(data.responses.some(response => response.advance));
      assert.equal(new Set(data.responses.map(response => response.id)).size, data.responses.length);
      for (const response of data.responses) {
        assert.ok(response.label && response.intro);
        assert.equal(typeof response.advance, 'boolean');
        assert.ok(!('answer' in response) && !('correct' in response));
      }
      if (section.includes('<video ')) assert.ok(data.videoPrompt?.endsWith('?'));
    }
  }
});

test('preserves optional single-answer quizzes, media and physical checks', () => {
  let quizzes = 0;
  for (const file of exercises) {
    const markdown = readFileSync(new URL(`../exercises/${file}`, import.meta.url), 'utf8');
    assert.match(markdown, /agent-instructions:/);
    for (const match of markdown.matchAll(/\{% pop-quiz\s+([\s\S]*?)%\}/g)) {
      quizzes += 1;
      assert.match(match[1], /mode="practice"/);
      assert.doesNotMatch(match[1], /mode="required"/);
      const choices = JSON.parse(match[1].match(/choices=(\[[^\n]+\])/)[1]);
      const answer = match[1].match(/answer="([^"]+)"/)[1];
      assert.equal(choices.filter(choice => choice.id === answer).length, 1);
    }
    for (const match of markdown.matchAll(/(?:src|poster)="\.\.\/([^"<>]+)"/g)) {
      assert.ok(existsSync(new URL(`../${match[1]}`, import.meta.url)));
    }
  }
  assert.equal(quizzes, 3);
  assert.match(readFileSync(new URL('../README.md', import.meta.url), 'utf8'), /b7fd6f2b465b8d32f9788a2bd1f3df39bf1401df/);
});
