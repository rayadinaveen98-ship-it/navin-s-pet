# Concept 3 — Facial / Idle Motion V04

**Date:** 2026-10-19  
**Status:** playable animation proof complete; art quality gate OPEN, not a Windows build.

## What changed since V03

V03 generated closed eyes using inpainting of the pupils; the resulting eyelids looked blurred and marker-like. V04 instead builds separate **temporary fur-textured upper-lid poses** from a nearby patch of the original approved Concept 3 illustration. It composites eyelids over the pupil progressively as they close, plus a thin cocoa crease at full closure. The original open-face artwork stays unchanged. This is a compositing study, not hand-painted final eyelid artwork.

The existing small rigid tail pivot remains in place. The head uses a restrained sub-degree rigid micro-tilt. The feet/body are kept grounded. No walking, voice, announcement, Done/Snooze reactions or running Windows overlay has been completed.

## Verified playable output

- **Video:** \`Navins_Pet_Concept3_Facial_Motion_V04.mp4\`
- H.264, 760 × 930, 30 FPS, 240 frames, **8.000 seconds** (verified with ffprobe).
- Companion GIF preview and close-up QA contact sheet.
- Three blink cycles; no continuous robotic blink loop.
- Motion difference compared with opening video frame (lossy decode):
  - Blink/face ROI ~9 average intensity units near fully closed moments.
  - Paw ROI ~0.11–0.16 units, consistent with codec noise; paws remain essentially fixed.
- Full reproducible, standalone Python renderer and exact locked source sheet shipped in conversation ZIP:
  \`Navins_Pet_Concept3_Facial_V04_Source_and_Preview.zip\`
- ZIP tested successfully for CRC integrity; SHA-256:
  \`b73dc6524b073cceb801c0e38e184e562d25fab2905d66ffa024151575ac5cf6\`
- GitHub contains smaller reusable eyelid-pose utility at \`tools/motion/eyelid_pose_v04.py\`. The **full video renderer and image assets are provided in the conversation source package**, not yet Git-committed as production assets.

## Quality assessment

**Improved:** no blurred-eye hole; there is visible fur structure across the closing eyelids, and half-closed poses are defined independently. Original eye art remains open and undisturbed between blinks.

**Still imperfect:** because the approved art was generated as a single flattened sheet, this method **clones nearby forehead texture** onto the eye. At full closure, the fur texture can look repeated or like a different patch of fur, and the lids/eyelashes are not authentically illustrated. Tiny head rotation can also expose hidden-edge limitations. Very subtle chest luminance change is not volumetric breathing. The actor is not transparent/motion-ready for direct import into WPF.

**Do not mark full idle animation approved solely because V04 is playable**.

## Next recommended product milestone

1. Obtain **proper layered master artwork** preserving exactly the approved Concept 3 puppy identity: original half-open/closed lids, eye surround, ears, head, behind-head fur, chest and tail. Draw/harmonize occluded regions, not only rotate/copy pixels.
2. Build a tiny Windows desktop overlay proof that plays a clean, restrained eyelid/tail/head idle as independent layers on a real desktop and confirm it does not steal focus.
3. Review real Windows video, fine fur edges, light/dark wallpapers, 100/150/200% DPI, and resource use.
4. After the idle scene earns acceptance, author foot-contact walk/stop/exit poses, then speech and reminder choreography.
5. Keep the main reminder engine/UI minimal. All work goes to \`rayadinaveen98-ship-it/navin-s-pet\` exclusively.

## Classification

- **Working:** offline playable 8-second rendered video; separate V04 texture-based eyelid pose generator.
- **Not yet working:** professional cutout/animation-ready eyelid layers, full head/ear articulation, real desktop pet, natural walking, speech, Windows installer.
