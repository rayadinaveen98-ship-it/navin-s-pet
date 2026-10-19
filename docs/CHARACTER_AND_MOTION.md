# Puppy 01 — Art and Motion Bible

## Artistic identity
Original 2D illustrated companion with warm ivory/apricot/cocoa tones and a restrained premium storybook style. The puppy should remain readable at 64–240 pixels, both light and dark backgrounds, and 100–200% Windows display scaling. Avoid an uncanny human-like face, flat sticker motion, stiff joints, or constant looping bobbing.

## Character and rig layers
The first editable source is `design/puppy-01/puppy-side-rig.svg` (560×440 draft study). Art groups are independently labeled for torso, tail, four legs, head, ears, eye shapes and mouth alternatives. It is **not a finished approved character or gait**.

| Layer | Role |
|---|---|
| Ground/contact shadow | Screen-space contact reference; independent of torso |
| Front/rear, near/far legs | Contact/passing action with foot plant and lift |
| Torso | Small pitch, squash/stretch and weight transfer |
| Head/neck | Gaze stabilization, look-up, constrained tilt |
| Ears/tail | Damped delayed follow-through, not random oscillation |
| Eyes/brows | Natural blink, restrained glance, happiness/concern |
| Mouth | Neutral, small/open talk, joy, optional mouth timing cues |
| Collar/tag | Secondary follow-through without clipping |

The final character needs coordinated side, 3/4 and turning reference frames with anatomical consistency, not simply flipped/morphed versions of an unrelated static illustration.

## Mandatory walk-cycle mechanics
1. Derive body travel from actual **stride displacement**.
2. During each stance phase, planted paws should remain fixed in **world coordinates** and transfer weight.
3. Passing phases involve visible foot lift, fore/hind alternation and appropriate draw order.
4. Torso motion follows footfall loading, with subtle vertical shift; don't fake locomotion using global sinusoidal translation.
5. Head anticipates the stop; body decelerates; last foot plants; idle begins from the actual settled pose.
6. Ears and tail follow the body's acceleration and stop with physically plausible lag/damping.
7. No discontinuities in elbow/knee, paw, collar, eye, shadow or overall silhouette during state changes.
8. Exit movement should use authored turn/leave poses. Do not represent a turn by suddenly flipping a static pet.

## Target animation states
- Hidden, anticipation/enter, walking, decelerating, settling, attentive idle, blinking, looking around, mouth small/open, happy response, snooze acknowledgment, turning, walking out, fully hidden.
- Interrupted/suspended/failed scene safely returns the scheduler to an actionable state.
- Alternate variants: full motion, reduced motion, no motion/text-only.

## Art production order
1. Refine final puppy silhouette and expression style in 3/4 pose.
2. Draw true side profile, front-facing and rear-facing consistent turnarounds.
3. Rig pivots; isolate frame-safe head, paws, ears, tail and facial layers.
4. Produce walk **contact left / passing left / contact right / passing right** key poses.
5. Add arrival anticipation, deceleration, planted stop, idle, talk, Done, Snooze, and exit keys.
6. Review actor at 64/120/180/240px on light, dark and busy wallpapers.
7. Export optimized WPF-compatible parts and sequences and document asset provenance.

## Timing targets (not measured)
- Enter 0.3–0.6 s; approach 1.2–2.5 s; settle 0.2–0.4 s.
- React 0.5–1.0 s; exit 0.8–1.8 s. Speech length depends on actual audio.
- 60 fps desirable on active Windows scene; profile rather than assume performance.

## Critical rejection criteria
Paws drift across the desktop while planted; body slides unrelated to gait speed; knees pop; instant frame-flipped turns; mouth moves before speech; frozen waiting; constant floating; abrupt post-action disappearance; skipped real-device testing.

## Production truth
Still-image concept art alone does not demonstrate motion. The current original rig is **draft** artwork; no authored walk cycle, full expression turnaround or Windows animation demo has yet been delivered.
