# Pet Announcement — Complete Interaction Specification

## Scene flow

```
HIDDEN
  -> PREPARING -> ENTERING -> TRAVELLING -> SETTLING
  -> SPEAKING -> WAITING
  -> [SAVING_DONE | SAVING_SNOOZE | DISMISSING | TIMING_OUT]
  -> REACTING (only after successful save)
  -> LEAVING -> HIDDEN
  -> NEXT_QUEUED
```

Each displayed scene has a unique session ID and cancellation token. Asynchronous speech, artwork, clock callbacks or persistence failures from a prior scene must not mutate a later scene.

### 1. Preparation
Read selected pet/animation/voice preferences; choose a valid placement within the foreground monitor work area; prepare audio or voice fallback; wait for renderer readiness. Never mark a reminder Done because it was shown.

### 2. Enter / travel / settle
Peek from safe edge; walk convincingly with planted feet; decelerate to a physically stable pose and face the user. Never animate a rigid image by sliding it across the screen. Pet scene occupies a bounded overlay, not an entire transparent click-stealing screen.

### 3. Speaking
Speak a natural, concise line based on **the user's reminder title** (e.g. “Time to work on your screenplay.”). Display the exact title clearly alongside controls. Speech starts after settling. Drive mouth expressions with actual timestamps when available, or with cached audio amplitude envelopes as explicitly approximate sync; random motion unrelated to audio is not acceptable. Enable Voice Off and replay/mute if appropriate.

### 4. Waiting
Keep a gentle alive pose with subtle breathing, occasional eye blinks and glances. Don't loop the full entrance animation or make the pet constantly bounce. Always expose Done, Snooze, Hide and voice mute through compact accessible controls.

### 5. Action
Save Done or Snooze **durably before** the pet celebrates/acknowledges it. If save fails, show retry and keep task actionable. Snooze reschedules, Done closes the current occurrence, Hide does neither.

### 6. Ignored reminder
Default quiet attention model: one optional gentle reannouncement after ~20 seconds *if user opts in*; if still unanswered, collapse/hide around ~45 seconds (configurable and pauseable while interacting) and retain Needs Attention state. Do not endlessly nag or auto-complete.

### 7. Leave
Play the correct corresponding response and an authored farewell/turn/outgoing motion, then fully release voice/timer/renderer resources. Handle a due queue serially; never stack multiple pets or overlapping voices.

## Desktop/Windows constraints
- No automatic foreground activation or keyboard focus stealing.
- Respect work area, per-monitor DPI, taskbar, screen change/disconnect, minimized/maximized/full-screen apps and accessibility motion settings.
- Session lock or suspend halts audio and scene; resume missed reminders appropriately.
- Ordinary Windows user processes cannot guarantee playback while power off or overlays on secure lock screen.
- Reduced motion, no sound, and text-only modes remain fully functional.
- Failure fallback must still provide actionable reminders.

## Audio & voice pipeline
- Default: locally generated/cached speech for scheduled titles; cache by content hash, voice ID, model version and settings (not by exposing titles in diagnostics).
- Compare offline neural voices against installed Windows voice fallback for naturalness, cold start, package size, CPU demand and language/pronunciation.
- One playback channel per active scene; cancel reliably on session lock, mute, dismiss or scene replacement.
- Viseme timing preferred where available; if audio-envelope mouth movement only, label and test it as approximate.
- No mandatory paid voice service.

## QA examples
- Short title; long title; Telugu/English mixed words; numeric times; edited reminder text; repeated reminders; rapid Done then Snooze; disk write failure; sleep during speech; multiple reminders due at once; changing monitors during scene; reduced motion; keyboard navigation and speech disabled.

**Design timing targets are not runtime measurements.**
