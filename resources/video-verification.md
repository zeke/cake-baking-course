# Batter demonstration: provenance and verification

This is one AI-generated test, not a recording of a tested recipe or proof of physical completion.

## Generation

- Model: [Kling 4.0 Flash on Replicate](https://replicate.com/kwaivgi/kling-v4-flash).
- Prediction: `zzh0z0men9rmr0d1xhn9d4x350`, succeeded 2026-11-18 UTC.
- Requested duration: 20 seconds. Delivered container duration: 20.042 seconds.
- Original output: H.264, 1284 × 716, AAC audio. Course copy: H.264, 1280 × 720, AAC audio preserved, fast-start MP4. A slight center crop after proportional scaling makes the course copy exactly 16:9; no speed or audio timing change.
- First-frame reference: generated hands-only kitchen still with orange silicone spatula. Poster: `assets/prepare-the-batter.png`, 1920 × 1080.
- Estimated generation price: $1.88 at the model page's $0.094 per output second for 720p without video input. This is an estimate, not an account billing receipt. No second video generation was made.

## Visual and playback checks

The MP4 fully decodes with ffmpeg without errors. Local Chrome playback was verified. A one-frame-per-second contact sheet shows stable framing, bowl, hands and orange spatula, with no visible text or cuts.

The model does not follow the requested single fold exactly: it produces about three gentle folding strokes in the first 7–8 seconds, then holds on the batter texture until the end. Treat this as a test worth reviewing, not a perfect production take. The final texture appears smoother than the requested few small lumps.

## Course rendering

The latest canonical [course specification](https://github.com/agentschools/course-spec/blob/main/SPEC.md) was checked at commit `c06dfd70a2f469d6ce0e1d023ad7316b7b986618`. It defines Markdown exercises but no special video component. The lesson therefore uses an HTML video element where supported and ordinary relative Markdown links as fallbacks. GitHub and other sanitizing Markdown viewers may strip the player or track; playback support in an enrolled school is not established. The repository remains private and cannot currently use public-repository school enrollment.

## Audio and captions

Two local speech-recognition passes (OpenAI Whisper base.en and small.en) independently transcribed the actual audio as: “Fold just until the dry streaks disappears. A few small lumps are fine.” Both detected an extra final “s” in “disappears,” unlike the requested script. The transcript and captions preserve that detected wording rather than silently rewriting the output. This is machine verification, not a human listening sign-off.

Caption timing combines word timestamps from both passes with measured audio activity: speech starts about 0.38 seconds in; the first phrase ends by about 3.23 seconds, and the second runs about 3.99–5.70 seconds. Cues span 0.350–3.300 and 3.950–5.800 seconds to include the whole phrases. They contain ordinary English text only, no positioning or speaker labels. Recognition found no additional speech. Audio after about 7.63 seconds is below -35 dB; the requested sustained soft kitchen ambience was therefore not strongly achieved. No claim of human-verified timbre or absence of all background music is made.

No paid transcription API was used. Local model downloads were needed for this verification.

Both English cues were visually verified in a local Chrome HTML video player at 1.0 and 4.5 seconds. The caption track loads and renders; controls and poster also work locally. This does not establish support in GitHub's sanitized Markdown renderer.
