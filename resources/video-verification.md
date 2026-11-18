# Generated course media: verification

These AI-generated demonstrations illustrate lesson techniques. They are not recordings of tested recipes or proof of learner completion.

## Prepare the batter, revision 2

- Model: [Kling 4.0 Flash on Replicate](https://replicate.com/kwaivgi/kling-v4-flash).
- Prediction: `kk0xc3aj7nrmy0d1xka8v2aq7r`, generated 2026-11-18 UTC.
- Duration: 20.042 seconds; 1280 × 720, H.264 video and AAC audio. Course copy re-encoded with fast-start metadata, with unchanged duration/audio.
- Poster: first frame of the revised video, matching its full-orange silicone spatula including handle. No text is baked into the image/video.
- One revised generation; estimated $1.88 at $0.094 per output second. This is an estimate, not a billing receipt. Initial version also cost approximately $1.88.
- One-frame-per-second visual review shows continuous folding/scraping through approximately 18 seconds and a short moving texture demonstration at the end. Stable bowl, hands and orange utensil; no visible cuts or on-screen text. Generated texture remains illustrative, not a recipe validation.
- Local Whisper small.en transcription matches the requested 46-word narration, including “disappear.” Speech begins approximately 0.60 seconds into the clip and ends around 19.5 seconds. Word timings plus audio activity were used for six short English WebVTT cues. No speaker labels or cue-positioning settings.
- Verification is machine-based speech recognition and visual inspection, not a human listening sign-off. No paid transcription API was used. Audio timbre and absolute absence of unwanted background sound are not human-verified.
- Full video decode and VTT parsing pass with ffmpeg/ffprobe. Relative lesson/media links resolve.

The original video, poster and two-cue captions remain recoverable from commit `561862b2ac8991e4db6f3f1981a8b940acda3403`. That version had a wooden spatula handle, short narration, a long still hold, and detected “disappears” instead of “disappear.” It is superseded, not represented as the current media.

## Course rendering

The canonical [course specification](https://github.com/agentschools/course-spec/blob/main/SPEC.md) was checked at commit `c06dfd70a2f469d6ce0e1d023ad7316b7b986618`. It defines Markdown exercises but no special video component. Lessons use HTML video where supported and ordinary relative Markdown links plus transcripts as fallbacks. GitHub and other sanitizing viewers may strip the player or track. Local browser playback does not establish support in an enrolled school. The repository is now public by owner request, but school enrollment and player support remain untested.

Local Chrome playback and visible rendering of the revised English caption track were verified.

## All six lesson media sets

Each current clip is 20.042 seconds at 1280 × 720 with H.264 video and AAC audio. Posters are first frames from their corresponding accepted clips. Each same-stem asset set contains `.mp4`, `.png`, `.en.vtt`, and `.transcript.txt`. Captions are transcribed from actual generated audio, not copied from requested narration. All six videos fully decode; all cue bounds/order and transcript text matches pass. Browser playback and visible English captions were checked separately for all six sets in local Chrome. No human audio-listening sign-off is claimed.

| Exercise | Verified insertion point | Correct local asset stem | Captions |
| --- | --- | --- | --- |
| [01-buy-the-ingredients.md](../exercises/01-buy-the-ingredients.md) | Gather the cake ingredients | `buy-the-ingredients` | 6 cues |
| [02-preheat-the-oven.md](../exercises/02-preheat-the-oven.md) | Prepare the pan | `preheat-the-oven` | 5 cues |
| [03-prepare-the-batter.md](../exercises/03-prepare-the-batter.md) | Fold the batter | `prepare-the-batter` | 6 cues |
| [04-bake-the-cake.md](../exercises/04-bake-the-cake.md) | Check the center | `bake-the-cake` | 5 cues |
| [05-decorate-the-cake.md](../exercises/05-decorate-the-cake.md) | Spread and decorate | `decorate-the-cake` | 5 cues |
| [06-serve-to-guests.md](../exercises/06-serve-to-guests.md) | Cut and serve | `serve-to-guests` | 6 cues |

For **each of the six exercises**, verification checked exactly one video embed, its correct local poster and MP4 source, English `kind="captions"` WebVTT track (`srclang="en"`, label `English`), controls, preload metadata, and separate fallback links to video, poster, captions and transcript. Checks reject cross-wired lesson assets and missing local files. Caption text matches the standalone and inline transcripts. File hashes, prediction identifiers, durations and byte sizes are in [media-manifest.json](media-manifest.json).

### Additional visual/audio review

- Ingredients: gathering and organizing, not an invented purchase or verified label/date. Labels remain illustrative; the learner must check real packaging.
- Preheat: pan greasing, parchment placement and greasing the paper. Both Whisper small.en and base.en independently recognize the spoken temperatures as 175°C and 350°F. The video does not claim the oven preheats in 20 seconds.
- Batter: revised all-orange utensil and longer narration, described above.
- Bake: the first result (`3t0htr16zdrmw0d1xke9psvx9r`) was rejected because it pulled a large chunk of cake out. One targeted retry (`c26zr8m7esrmw0d1xkft3ez96m`) shows a clean skewer and intact cake with mitt protection and is the only bake clip installed.
- Decorate: spreading frosting on a cooled cake, finishing a swirl and sprinkles; orange utensil maintained.
- Serve: the starting image has a pre-cut wedge, so the demonstration transfers it to a plate. It does not demonstrate the cutting step or imply guests' allergy clearance.

These are separate generated illustrations: cake size/frosting appearance is not perfectly continuous between lessons. Some clips settle briefly after the action finishes rather than moving every final frame. No claims of tested food results or physical learner completion should be inferred.

### Cost and retained versions

Eight 20-second video predictions were made in total: initial batter, revised batter, five other lessons, and one targeted bake retry. At 20.042 seconds each and the model page's $0.094 per output second, the video-generation estimate is **$15.07 total**. This is not a billing receipt and excludes poster/image generation costs, which the image tools did not report. No paid transcription API was used. No additional video retries were made. Original batter remains in git history; rejected bake output and source generation records remain in the local ignored work area, not in the lesson assets.
