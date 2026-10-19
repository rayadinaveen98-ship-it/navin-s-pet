# Windows Architecture — Navin's Pet (Proposed)

## Build target
Native Windows .NET 10 desktop project using WPF and C#. Initial implementation should avoid mandatory hosted services or any paid TTS account.

## Major modules
1. **Reminders.Core** — immutable reminder IDs, title, due date/time, optional recurrence, occurrence state, Done/Snooze/Needs Attention, scheduling calculations; unit-testable without WPF.
2. **Reminders.Store** — local durable JSON/SQLite-based storage chosen after prototyping; atomic writes/transactional updates, automatic backup and schema versioning. Never claim saved state before durable commit.
3. **Reminders.Scheduler** — lightweight resident per-user Windows tray process; timer-based due selection, catch-up on startup/wake/unlock, serialize simultaneous alerts and record missed/unanswered events.
4. **Companion.Actor** — transparent bounded non-focus-stealing WPF overlay with state machine, safe placement, per-monitor DPI adaptation, z-order/foreground checks, input hit-testing and accessible fallback.
5. **Companion.Motion** — authored 2D part/pose playback; measured stepping and paw world position, deceleration, gaze/ear/tail follow-through, motion-off variants and resource cancellation.
6. **Speech** — offline synthesizer adapter / Windows fallback, optional render-ahead caching, playback, mouth-track cue output and audio interruption.
7. **UI** — small main window: quick create, upcoming/attention views, pet preview, essential settings.
8. **Diagnostics** — bounded local error logs without reminder titles; crash containment, user-readable recovery.

## Suggested repository structure
```text
NavinsPet.sln
src/
  NavinsPet.Windows/
  NavinsPet.Core/
  NavinsPet.Motion/
  NavinsPet.Speech/
tests/
  NavinsPet.Core.Tests/
  NavinsPet.Motion.Tests/
  NavinsPet.Windows.SmokeTests/
design/
  puppy-01/
docs/
  PRODUCT_BLUEPRINT.md
  CHARACTER_AND_MOTION.md
  REMINDER_PERFORMANCE.md
  ARCHITECTURE.md
  ROADMAP.md
  QA_ACCEPTANCE.md
  PROJECT_STATUS.md
```

These are target directories, **not a claim that source modules already exist**.

## Important technical decisions
- Avoid full-screen transparent window with active hit testing; the pet needs a small rectangle plus independently accessible controls.
- No timers controlled by UI visibility for reminder reliability; minimize/close keeps tray scheduling active unless explicitly exited.
- A single session token owns overlay, active TTS and motion; canceled events are safely ignored.
- Reminders due while locked/sleeping are processed when Windows is available; do not claim secure-desktop overlay privileges.
- Animation render loop only runs while character is visible, and must not burn CPU when minimized/hidden.
- Keep data entirely separate from other desktop reminder projects. **No automatic migration or coupling to legacy app databases.**

## Build and delivery gate
Windows GitHub Actions: dotnet restore/build/test, publish portable win-x64 EXE, optional Inno Setup installer, automated clean install/reinstall/uninstall preserving user data. Passing CI does not replace hands-on desktop recording, TTS audibility, mixed-DPI, lock/wake, full-screen and resource testing.

## Security and distribution
No reminder title in telemetry; no always-on microphone; no executable code in user art packs. Offline model licenses, downloadable dependencies, signing, installer warnings and third-party art rights reviewed before release.
