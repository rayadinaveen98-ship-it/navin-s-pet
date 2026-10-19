# Navin's Pet — Acceptance Gates & Test Checklist

## Gate A — Art
- [ ] Originality and distribution rights checked.
- [ ] Puppy silhouette recognizable at 64px; eyes/muzzle readable.
- [ ] Layered source files allow independent articulation.
- [ ] Consistent side, front, 3/4 and exit pose turnaround.
- [ ] Transparent backgrounds free of seams and incorrect matte/halo.
- [ ] Light/dark/busy wallpapers and 100–200% DPI accepted.

## Gate B — Motion
- [ ] Normal and 0.25x recorded Windows footage reviewed.
- [ ] Stationary planted paw during stance; no skating.
- [ ] Stride spacing consistent with movement speed and body weight.
- [ ] Natural acceleration and deceleration; settled feet before speech.
- [ ] Correct secondary movement and natural nonrepetitive idle.
- [ ] Unique gentle Done, Snooze and exit sequences; no abrupt disappear.
- [ ] Reduced/zero motion modes work and are pleasant.

## Gate C — Speech
- [ ] Natural pre-generated or local speech of title with acceptable initial latency.
- [ ] Speech audible at normal PC volume; independently configurable.
- [ ] Mouth cues follow real audio rather than an unrelated animation loop.
- [ ] Test Telugu-English names, numerals, abbreviations, long titles, empty/invalid text.
- [ ] Cancels speech on mute, lock, hide, new-session cancellation.

## Gate D — Reminder reliability
- [ ] Once/daily/weekly recurrence with correct per-occurrence state.
- [ ] Done/Snooze commit persists across close, crash, reboot.
- [ ] Failed disk save does not trigger fake Done animation.
- [ ] Missed/unanswered items recover in Needs Attention.
- [ ] Two or more reminders due at once serialize with one voice at a time.
- [ ] Tray scheduling survives main-window hide.
- [ ] Restart and Windows sleep/lock/unlock behavior documented and tested.

## Gate E — Desktop UX
- [ ] No focus theft.
- [ ] No full-display input-blocking invisible overlay.
- [ ] Minimally intrudes over video editing/browser/game windows.
- [ ] Safe taskbar and monitor-placement constraints; multi-monitor/DPI.
- [ ] Simple one-window UI with no unnecessary copy.
- [ ] Keyboard/assistive accessibility and large text/responsive resizing.
- [ ] CPU, RAM, GPU and battery usage profiled during animation and idle.

## Gate F — Distribution
- [ ] Build, tests and packaging CI green.
- [ ] Unsigned status clearly disclosed until signed.
- [ ] Portable and installer smoke-tested on actual Windows.
- [ ] Installer upgrades/reinstall/uninstall do not wipe stored reminders.
- [ ] Independent storage path, no automatic reads or edits to unrelated applications.
- [ ] Third-party asset/model licenses checked; no paid service required for base function.

**Current status:** Specifications and draft vector exist. Art/motion/voice/desktop/release checkboxes stay **unchecked** until evidence is available.
