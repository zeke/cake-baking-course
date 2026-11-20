# Bake Your First Cake

An example course for experimenting with agent-guided learning: six small steps from buying ingredients to serving a cake. Start with [COURSE.md](COURSE.md).

This is a public experimental course for trying agent-guided lessons and media. It uses the [Agent Schools course format](https://github.com/agentschools/course-spec/blob/main/SPEC.md) plus the HTML authoring experiment below. Public visibility is not evidence of tested school enrollment or renderer support.

[Interaction examples](resources/batter-interactions.md) explore three ways to finish the batter step. All six exercises now include a 20-second generated demonstration, matching poster, English captions and actual-audio transcript. [Media verification](resources/video-verification.md) documents checks and limitations; [the manifest](resources/media-manifest.json) records exact assets. No learner progress is stored in this repository.

- [Buy the ingredients](exercises/01-buy-the-ingredients.md)
- [Preheat the oven](exercises/02-preheat-the-oven.md)
- [Prepare the batter](exercises/03-prepare-the-batter.md)
- [Bake the cake](exercises/04-bake-the-cake.md)
- [Decorate the cake](exercises/05-decorate-the-cake.md)
- [Serve to guests](exercises/06-serve-to-guests.md)

The recipe is an original, untested teaching example, not a kitchen-tested recipe. Validate it with a test bake before using this course for real instruction. No baking or live school enrollment was performed during authoring.

## HTML authoring experiment

This branch puts four kinds of learning blocks directly in the exercises: an unscored question, a single-answer quiz (including true/false), matching, and a teach-back with a short rubric. They use ordinary HTML with a small set of data attributes.

The source stays open-book. Matching pairs and quiz answers are visible to anyone reading it. Teach-back criteria guide a conversation, not automatic grading. None of these blocks proves that a learner baked anything.

A school would parse the allowed blocks as inert data and render its own interface. This experiment has no renderer, script evaluation, custom-element runtime or form submission. Generic Markdown viewers may strip attributes, so they cannot be relied on for interactive behavior. Existing videos are unchanged.

This is an alternative to the [Markdoc proposal](https://github.com/agentschools/course-spec/pull/11), not an adopted course-spec feature. See [AGENTS.md](AGENTS.md) for the local checks.

## Conversation sections

Each exercise has two authored conversation sections, separated by a Markdown thematic break. Each ends with a leading question, separate from the optional scored practice quizzes. [The section resource](resources/sections.json) gives those sections stable IDs, context-specific video prompts and unscored response branches. A learner can ask for a particular explanation or pause over an unresolved check, and their selected response changes the next introduction. Their written observations remain part of the conversation.

This is an experimental convention local to this course. It adds no frontmatter fields or executable markup and is not an adopted course-spec feature. The section resource supplies an authored fallback for a renderer without a live model; other agents can use the prose questions directly. A response never verifies that a kitchen action happened.
