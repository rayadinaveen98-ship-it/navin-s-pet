# Navin's Pet — Project Status & Handoff

**Updated:** 19 October 2026  
**Canonical GitHub repository:** `rayadinaveen98-ship-it/navin-s-pet`  
**Canonical URL:** https://github.com/rayadinaveen98-ship-it/navin-s-pet  
**Platform:** Windows desktop first  
**Status:** Phase 1 original-art **draft foundation**, not working application  
**Default branch:** main

## Latest decision — 2026-10-19: reject V04 motion and reset pipeline
**User review:** V04 still looks uneven and imperfect; no V01–V04 motion is visually approved. **Approved Concept 3 character artwork remains locked as visual reference**. Stop deriving production head/eye/tail motion by inpainting, piecewise masks or global 2D pixel warping of that flattened sheet.

**Next route:** genuinely author animation-ready independent painted layers; trial Krita/Photoshop-like layer tools and **Moho Pro** rigging; evaluate **Spine** as alternate. Do not buy tools or call motion complete without normal/quarter-speed actual rigged video acceptance. Export transparent PNG sequence/atlas for native Windows overlay only after an approved rig exists. See [animation pipeline reset](ANIMATION_PIPELINE_RESET.md).

## Key decision
Navin's Pet is a **new and independent** project. Do not add, maintain or merge Navin's Pet source into any earlier pet reminder repository. Do not reuse previous PetPing walking experiments that looked unnatural. We are only carrying forward human learning, product requirements, and separately authored original artwork; we are not importing existing app data or past implementations.

## Core promise
A premium aesthetic illustrated puppy (later cat and butterfly) walks on to the desktop with believable planted-foot gait and organic secondary movement, stops, naturally announces the user's reminder title, continues subtle lifelike idle while waiting, reacts to Done/Snooze, and exits smoothly. The Windows manager is one small uncluttered reminder window plus quiet tray service.

## Delivered in this new repo
- Project README with product identity, features, architecture direction and limitations.
- Product blueprint: `docs/PRODUCT_BLUEPRINT.md`.
- Original puppy animation requirements: `docs/CHARACTER_AND_MOTION.md`.
- Reminder show/speak/respond choreography and state machine: `docs/REMINDER_PERFORMANCE.md`.
- Proposed Windows technical layout: `docs/ARCHITECTURE.md`.
- Staged implementation plan: `docs/ROADMAP.md`.
- Release and animation acceptance checklist: `docs/QA_ACCEPTANCE.md`.
- Editable **draft** layered puppy 3/4-view SVG source: `design/puppy-01/puppy-side-rig.svg`.
- Local static multi-background art-review HTML page: `design/puppy-01/art-review.html`.
- Character study notes: `design/puppy-01/README.md`.
- A project .gitignore for .NET development.

## Still not delivered
- Full professional puppy concept/model approved by the user.
- Consistent front/side/rear views, eyelid poses, final expression pack and keyframe sprites.
- Functioning foot-contact gait, 60fps Windows animation, entrance/exit movie or screen recording.
- Local neural TTS engine, real mouth synchronization or voice QA.
- Windows app, reminder scheduler integration, settings UI, installer and real-device testing.

## Immediate next engineering milestone
1. Review/refine puppy silhouette and anatomy.
2. Author reliable editable front/side/3/4/turn poses and four principal walk/contact/pass keyframes with anchored paws.
3. Develop first transparent Windows motion-only test harness in this repository.
4. Record complete entry, travel, stop, idle and exit on a physical Windows desktop; test at normal and 0.25x playback.
5. Only after that passes, connect natural speech, title rendering and reminder actions.

## Scope safeguards
- **No coupling** to old repo or user storage directories.
- Don't report storyboards/concept images as working motion.
- Never claim compiled EXE, installer, passing CI or physical-device success until verified.
- Keep open blockers visible; quality and simplicity outrank speed.

## Last known progress
Repository initialized with phase-1 specification and draft SVG. Project is ready for art refinement and dedicated Windows motion prototype. No Windows build exists yet.


## 2026-10-19 — Targeted tail motion proof v02
- A real **5.2-second MP4 and looping GIF** generated using the user's locked Concept 3 puppy.
- Replaced prior rubber-like pixel deformation with **rigid pivoted tail sprite rotation**; rest of body and paws held stationary.
- Objective file check: **156 frames at 30 fps**, H.264 820×960. Pixel differences are concentrated near tail, not the head/paws.
- Tested rendering pipeline uses source from the conversation-delivered source/video ZIP. A simplified standalone reference implementation is committed as `tools/motion/tail_pivot_v02.py`.
- See `docs/MOTION_PROTOTYPE_V02.md` for caveats, exact scope, numerical verification and next tasks.
- **Not yet accepted as final art/animation:** masking from flat art leaves potential fine fringe; blink, head movement, breathing, walking, natural voice and actual WPF app still pending.
- Original approved concept sheet and demo binaries are in the conversation artifact ZIP, NOT tracked as GitHub binary assets yet.


## 2026-10-19 — Concept 3 complete idle proof V03

**Completed a 9.00-second playable offline prototype** from the user-approved Concept 3 puppy. Generated MP4 (H.264, 760x930, 30 fps, 270 frames), GIF, visual-QC contact sheet, blink-QC still, and a verified ZIP with the **actual runnable Python prototype sources**, original approved image, and media. Source/media bundle is attached in the relevant ChatGPT conversation, not yet committed as binary assets.

The timed scene combines three 160–180 ms reconstructed eyelid blinks, very small rigid head rotations, the v02 fixed-shape rotating tail, and subtle chest light variation. Paws remain mostly stationary; no walking, natural speech, real Windows overlay, completed rig or installer exists.

**Important quality gate remains open:** Blink reconstruction looks soft/painted over, rather than professionally layered; fur seam and occlusion from the flattened source image may be imperfect. Render feasibility does not mean the fully lifelike character goal is achieved. Do not declare the idle animation visually approved until user acceptance. Next: hand-authored eyelid, under-head, under-tail and body layers consistent with locked Concept 3, then re-render and integrate into Windows.

See [idle V03 report](IDLE_MOTION_V03_REPORT.md) for precise limitations, QA and the path forward. All development stays solely in this repository.


## 2026-10-19 — Concept 3 textured eyelid / face V04 study
- **Rendered and verified** 8.0s H.264 760x930 @ 30fps (240 frames), plus GIF and eye-pose QA images, preserving the user-locked Concept 3 identity.
- Replaced prior pupil-inpainting blur with experimental fur-texture eyelids derived from adjacent painted fur. A small closed-lid crease is visible; micro head tilt and prior rigid tail swing remain.
- QA: moving face ROI differs by ~9 intensity units at blinks, paw region remains essentially unchanged (~0.11–0.16, codec noise).
- Reproducible standalone rendering script, exact reference sheet, video/GIF and QC images provided in conversation ZIP: \`Navins_Pet_Concept3_Facial_V04_Source_and_Preview.zip\`, CRC verified, SHA256 \`b73dc6524b073cceb801c0e38e184e562d25fab2905d66ffa024151575ac5cf6\`.
- Source reusable eyelid pose tool now committed to \`tools/motion/eyelid_pose_v04.py\`. Technical report at [V04 report](IDLE_MOTION_V04_REPORT.md).
- **Art acceptance still open:** eyelids are fur-texture compositing from a flat sheet, not properly artist-painted separate rig parts. No real WPF animation, walking, speech or installer claim. Need art segmentation and real desktop proof after review.
