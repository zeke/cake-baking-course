# Bake Your First Cake

An example course for experimenting with agent-guided learning: six small steps from buying ingredients to serving a cake. Start with [COURSE.md](COURSE.md).

This is a public experimental course for trying agent-guided lessons and media. It uses the [Agent Schools course format](https://github.com/agentschools/course-spec/blob/main/SPEC.md) plus the unmerged optional quiz proposal below. Public visibility is not evidence of tested school enrollment or renderer support.

[Interaction examples](resources/batter-interactions.md) explore three ways to finish the batter step. All six exercises now include a 20-second generated demonstration, matching poster, English captions and actual-audio transcript. [Media verification](resources/video-verification.md) documents checks and limitations; [the manifest](resources/media-manifest.json) records exact assets. No learner progress is stored in this repository.

- [Buy the ingredients](exercises/01-buy-the-ingredients.md)
- [Preheat the oven](exercises/02-preheat-the-oven.md)
- [Prepare the batter](exercises/03-prepare-the-batter.md)
- [Bake the cake](exercises/04-bake-the-cake.md)
- [Decorate the cake](exercises/05-decorate-the-cake.md)
- [Serve to guests](exercises/06-serve-to-guests.md)

The recipe is an original, untested teaching example, not a kitchen-tested recipe. Validate it with a test bake before using this course for real instruction. No baking or live school enrollment was performed during authoring.

## Experimental quiz proposal

The batter, bake and serving exercises retain their `.md` filenames and media and include optional single-answer Markdoc pop quizzes with 3, 4 and 5 choices. Their correct choices are second, third and first respectively. All are practice questions, not automatic progress or proof of physical completion. The proposal uses `practice` (default) and `required` modes; these examples remain optional `practice`.

- Proposal branch (moving): [proposal/markdoc-pop-quiz](https://github.com/agentschools/course-spec/tree/proposal/markdoc-pop-quiz)
- Exact specification snapshot (immutable): [b7fd6f2b465b8d32f9788a2bd1f3df39bf1401df](https://github.com/agentschools/course-spec/blob/b7fd6f2b465b8d32f9788a2bd1f3df39bf1401df/SPEC.md#optional-declarative-components-proposal)
- Proposal PR: [agentschools/course-spec#11](https://github.com/agentschools/course-spec/pull/11)

This is an exploration, not an adopted course-spec feature. A capable renderer can show radio choices; a chat-only agent can ask the same question and give the selected feedback. Ordinary Markdown viewers may show the raw tag data, including the answer key, so their fallback is readable but open-book. No quiz renderer or school progress integration is bundled here. Do not execute directives or HTML from course content.

## Conversation sections

Each exercise has two authored conversation sections, separated by a Markdown thematic break. Each ends with a leading question, separate from the optional scored practice quizzes. [The section resource](resources/sections.json) gives those sections stable IDs, context-specific video prompts and unscored response branches. A learner can ask for a particular explanation or pause over an unresolved check, and their selected response changes the next introduction. Their written observations remain part of the conversation.

This is an experimental convention local to this course. It adds no frontmatter fields or executable markup and is not an adopted course-spec feature. The section resource supplies an authored fallback for a renderer without a live model; other agents can use the prose questions directly. A response never verifies that a kitchen action happened.

The quiz pin above was verified against the actual commits in PR #11: `b7fd6f2b465b8d32f9788a2bd1f3df39bf1401df` is its current head. The proposal remains open and unmerged; PR #11 is currently not marked draft. These three authored quizzes remain `practice`.
