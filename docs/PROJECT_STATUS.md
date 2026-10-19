# Navin's Pet — Project Status & Handoff

**Updated:** 19 October 2026  
**Canonical GitHub repository:** `rayadinaveen98-ship-it/navin-s-pet`  
**Canonical URL:** https://github.com/rayadinaveen98-ship-it/navin-s-pet  
**Platform:** Windows desktop first  
**Status:** Phase 1 original-art **draft foundation**, not working application  
**Default branch:** main

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
