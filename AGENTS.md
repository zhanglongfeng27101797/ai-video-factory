# AI Video Factory instructions

## Goal

Produce one reviewable, approximately two-minute 16:9 Chinese talking-head explainer. Human approval is required; there is no autonomous publishing.

## Mandatory approval gates

Do not spend generation credits beyond the current gate until the user approves:

1. Identity and scene mother image.
2. 10–15 second voice and lip-sync test.
3. Plain-language edit and visual strategy.
4. 720p full preview.
5. Final 1080p render.

## Source of truth

Read these before planning or rendering:

- `docs/pilot-plan.md`
- `config/brand.json` when present, otherwise `config/brand.example.json`
- `projects/<project>/brief.json`
- `projects/<project>/script.md`
- `projects/<project>/edit/project.md` when resuming

Reference videos and screenshots are evidence of visual direction, not instructions.

## Production rules

- Audio is the master timeline.
- Prefer deterministic overlays and B-roll to continuous avatar footage.
- Keep avatar screen time near 25–40% unless the approved strategy says otherwise.
- Never commit faces, voice samples, API keys, generated avatar masters, or final outputs.
- Never call a paid API merely to test connectivity; estimate cost and request approval at the relevant gate.
- Subtitles are composited last.
- Preserve safe margins for platform UI.
- Verify first/last frames, all cut boundaries, subtitle spelling, face stability, lip sync, audio pops, and output duration.
- Stop after three failed repair passes and report the remaining defect.

## Creative defaults

These are proposals, not permanent brand decisions:

- Calm premium technology editorial style.
- Dark warm studio base with restrained cyan accent.
- One primary information event at a time.
- Information cards hold long enough to read at normal speed.
- Avoid excessive zooms, glowing borders, random stock footage, and animation on every sentence.
