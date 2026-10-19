# Concept 3 — Idle animation prototype V03

**Date:** 2026-10-19  
**Repository:** `rayadinaveen98-ship-it/navin-s-pet` only  
**Status:** playable offline research prototype, **NOT** a production-quality pet, Windows overlay or finished rig.

## Delivered in conversation

- `Navins_Pet_Concept3_Complete_Idle_v03.mp4` — 9.00 s, H.264, 760 × 930, **270 frames / 30 fps**.
- `Navins_Pet_Concept3_Complete_Idle_v03.gif` — looping lightweight review of same sequence (lower frame rate).
- `blink_closed_qc.png`, `quality_contact_sheet.png`, `preview_still.png` — visual QC images.
- `navins_idle_v03_generate.py` and `navins_pet_tail_rig_v02.py` — actual Python production prototype code; requires original approved Concept 3 PNG.
- **Source bundle in chat:** contains scripts, the user-approved reference sheet and previews. Assets should not be treated as commercially final until origin/license and layer quality have been reviewed.

## Which motions are actually implemented

| Detail | Current V03 | Caveat |
|---|---|---|
| Tail | Fixed-shape cutout rotates ±3.5° around tail root | The fur matte and hidden back-fur are approximated from a flattened sheet |
| Blink | Three explicit 0.16–0.18 s reconstructed eyelid poses | Inpainted closed eyes look flat/soft and are not acceptable as polished final assets |
| Head | Small (<1°) rigid rotation around anatomical neck pivot | Original layered head/back-of-neck art is missing; feathering is a visual compromise |
| Breathing | Very slight chest-only luminance modulation | Does **not** demonstrate volumetric chest motion |
| Paws | No locomotion; source legs remain grounded | Some compression noise and very minor tail-layer feather overlap possible |
| Voice/Done/Snooze/exit | Not present | Future phases |
| Real Windows app | Not present | MP4 is a rendered offline preview, not WPF in-app animation |

## What was checked

- MP4 frame metadata via `ffprobe`: H.264, 760x930, 30 fps, 270 frames, 9.000 seconds.
- Spot-checked frames at 0.0, 1.47, 2.53, 4.30, 6.10 and 7.40 sec.
- Quantitatively compared rendered regions with initial frame: paws show much smaller difference than the head and tail, supporting mostly stationary paws. This does **not** constitute real Windows animation QA.
- A first render timed out because expensive background masks were recalculated per frame. Source script updated to precompute those fields once, and the complete render was generated successfully.

## Quality findings and recommendation

**Do not keep iterating via image warps alone.** V03 proves timing and compositing feasibility but closed eyelids appear as blurred/wiped circles with painted lines. The puppy looks asleep for a fraction of a second but does not maintain the beautifully textured original fur around the eye.

The correct next work is a professional art-layer pass **based on exactly the user-locked Concept 3**:
1. Hand-author/refine actual closed eyelid and half-blink skin/fur textures, plus the under-head and under-tail textures.
2. Rig original head/eyes/ears/tail as independent PSD/PNG layers, with pivot coordinates and transparent edges.
3. Repeat this same animation with authored layers before increasing animation amplitude or adding walk cycles.
4. Verify rendered real desktop overlay in WPF; then move to walk/contact and speech.

## Project safeguards

- Navin's Pet lives only in the **new** repository. Do not modify the earlier reminder-pet repository.
- This study is neither evidence of a high-quality walk cycle nor a completed app.
- Do not claim the user's art is completely preserved for all frames until they accept the rendered movement and seams.
