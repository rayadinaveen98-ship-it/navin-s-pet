# Navin's Pet — Product Blueprint
Status: v0.1 direction locked for development; interface and character visuals still under review (19 October 2026).

## Purpose
Navin's Pet exists to make desktop reminders feel like a brief personal encounter with a gentle animated companion, not a distracting notification center.

## Primary use case
A creator or any Windows user works in another application. At the scheduled time, a pet approaches from a safe edge, stops, speaks the reminder name clearly, remains calmly animated, and offers **Done** or **Snooze**. After acknowledging, the pet gives a natural response and leaves. The desktop stays usable at all times.

## Non-negotiable product principles
1. **The pet performance IS the feature** — convincing movement, expression and audio coordination are more important than UI ornaments.
2. **Minimal, professional interface** — one small window for reminders and lightweight settings; no paragraphs explaining every element.
3. **Trustworthy reminders** — no completed status until saving succeeds, no silent loss of ignored reminders.
4. **Respectful desktop presence** — no focus theft, unnecessary overlays, repeated nagging, or blocking important application controls.
5. **Original illustration** — expressive, aesthetic, readable at small sizes, with consistent front/side/back poses.
6. **Local-first, affordable** — usable offline, no mandatory login, no subscription or paid API to create reminders.
7. **Accessible** — motion off, voice off, readable text-only fallback, simple keyboard operation.

## MVP scope
### Main window
- App title **Navin's Pet**.
- One visible quick-create form: reminder title, date, time, repeat (once/daily/weekly).
- Upcoming reminder list: title, due time, edit/delete, and understandable status.
- Needs Attention list for unanswered/missed reminders.
- A compact pet choice (Puppy initially) and Voice On/Off.
- Essential Settings: startup at login, pet position/size, motion intensity, repeat announcement and snooze duration, locally stored data/help.
- System tray allows Show, Add Reminder, Pause/Mute, Exit.

### Pet scene
- Pet physically travels (not static picture sliding), settles, speaks, waits with subtle organic idle movement, reacts to Done/Snooze, and exits.
- One active pet at a time; additional reminders queue instead of overlapping.
- User can dismiss/hide the pet without falsely completing the reminder.
- Pet/voice/render failures show actionable fallback reminders.
- Never continue speaking while the session is locked.

### Out of scope initially
Pet feeding/care, streaks, dashboards, accounts, cloud sync, AI chat, mobile app, additional pet species until puppy has passed review, and advanced arbitrary schedules.

## Character family
- **Puppy — V1:** welcoming, attentive, soft step-bounce from foot contact, floppy ears, warm alert gaze.
- **Cat — later:** deliberate steps, curious gaze, independent tail/ears.
- **Butterfly — later:** flight paths, flutter dynamics, hovering/landing rather than a reused walk cycle.

## Main product screens
Only **Reminders** and minimal **Settings** are necessary. Pet customization may be a small section/popup under Settings. Avoid adding navigation pages unless indispensable.

## Success criteria
- A nontechnical user can create a reminder in seconds.
- Full pet scene is coherent and natural, not a collection of disjoint effects.
- Speech starts promptly after settling and is intelligible.
- Done/Snooze are unmistakable and genuinely persisted.
- App stays responsive and quiet between alerts.
- The user approves real Windows recordings of complete scene before motion is shipped.

## Open product questions to evaluate in prototypes
- Optimal desktop pet footprint and safe corners in common apps.
- Whether initial installation bundles a local neural model or downloads an optional model once with consent.
- Voice quality vs offline model footprint and CPU demands.
- Exact ignore/auto-dismiss policies after real usage feedback.
