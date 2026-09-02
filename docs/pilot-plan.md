# Two-minute pilot: requirements and uncertainty gates

## Definition of done

The pilot is accepted when it communicates one complete idea in 105–135 seconds, looks intentional at normal playback speed, and contains no obvious identity drift, lip-sync failure, subtitle error, black frame, audio pop, or unreadable card.

Target delivery: 1920×1080, 30 fps, H.264 video, AAC audio, 16:9.

## What Codex can decide

- Convert the approved script into hook, problem, explanation, example, and close.
- Propose pacing, avatar/B-roll balance, card placement, subtitle chunks, transitions, and music restraint.
- Build deterministic cards, diagrams, captions, transitions, edit decisions, renders, and QA evidence.
- Reuse approved brand and identity assets without asking the same questions again.

## What requires the user's judgment

- Whether the generated person still looks like the user.
- Whether the cloned voice feels like the user rather than merely sounding similar.
- Whether the studio scene matches the desired public image.
- Whether the script's claims and tone should be published under the user's identity.
- Final acceptance of the preview.

## Gate 1: identity and mother image

Input: preferably 3–5 recent, unfiltered photos with one clear frontal image, plus optional three-quarter and neutral-expression views. Ten to twenty photos are useful only if they are consistent; AI-generated identity variants must not be fed back as equal truth because errors compound.

Process: preserve facial identity from real references, generate 2–4 16:9 studio-scene candidates, and select one approved mother image. Additional generated images are style candidates, not an identity training set.

Pass criteria:

- Recognizable without explanation.
- Stable eye spacing, face shape, hairline, teeth, hands, and accessories.
- Natural seated posture and plausible desk geometry.
- Enough negative space for cards and captions.
- No text baked into the background.

Main uncertainty: identity drift and synthetic skin. Resolve this before buying long avatar generation.

## Gate 2: voice and lip sync

Input: one approved 45–60 Chinese-character test sentence and clean real voice samples.

Output: 10–15 seconds at low-cost preview quality.

Pass criteria:

- First viewing feels like the user.
- Consonants and sentence endings are natural.
- No obvious mouth lag, frozen teeth, face shimmer, or unnatural blink loop.
- Loudness is consistent and free of clipping.

Main uncertainty: a good still image does not guarantee good mouth motion. If it fails, change the mother image or avatar mode before proceeding.

## Gate 3: content and visual strategy

Codex submits a plain-language plan before editing: narrative beats, estimated durations, avatar windows, B-roll needs, information cards, subtitle style, palette, and estimated paid generation cost.

Default two-minute shape:

- 0–8s: avatar hook.
- 8–30s: problem, avatar plus one information card.
- 30–75s: explanation using diagrams, screenshots, and B-roll; avatar appears selectively.
- 75–105s: example or proof.
- 105–120s: avatar conclusion and call to action.

Main uncertainty: editorial taste. Resolve it with a strategy document, not repeated full renders.

## Gate 4: 720p preview

Review the whole story, timing, card readability, subtitle spelling, avatar continuity, and music level. Feedback is recorded in `projects/<project>/edit/project.md`.

## Gate 5: final render

Render 1080p only after preview approval. Produce final video plus a QA report containing duration/codec checks and sampled review frames.

## Cost-control rule

For Avatar IV/V API estimates, use current published rates when executing. The bundled estimator uses a configurable default of USD 0.05/sec for Photo Avatar and USD 0.0667/sec for Digital Twin. It is an estimate, not a billing quote. Budget at least one short test and a 30–50% retry reserve.
