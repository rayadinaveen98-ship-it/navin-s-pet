# Navin's Pet 🐾

**A little friend who makes sure you remember.**

Navin's Pet is a **Windows desktop reminder companion** built around one simple experience: a beautifully illustrated pet comes onto the screen, walks or flies naturally to a comfortable spot, announces your reminder name, waits for your response, reacts to **Done** or **Snooze**, and leaves.

The app itself should be **small, clean, elegant, and almost invisible until needed**. This is not a pet-care game, a productivity dashboard, or an unnecessarily complicated notification system.

> **Development status — 19 October 2026:** Concept locked; original puppy art/rig study and specifications prepared. Real Windows animation, natural offline speech, the redesigned app, and installer are **not yet completed**. See [PROJECT_STATUS.md](docs/PROJECT_STATUS.md).

## Product experience

1. **Reminder due:** a single pet scene is prepared without stealing keyboard focus.
2. **Arrive:** the selected pet enters from a safe screen edge using genuinely authored motion.
3. **Approach & settle:** its feet contact the ground correctly, it decelerates and looks toward you.
4. **Announce:** it naturally speaks the reminder's name while the mouth and expressions follow the real speech timing.
5. **Wait:** it remains subtly alive, with gentle blinking/breathing, and shows minimal **Done** / **Snooze** controls.
6. **Respond & leave:** the action is saved first, the pet gives a short fitting reaction, then walks or flies away.

Ignored reminders remain recoverable as **Needs Attention**, rather than being silently considered completed.

## Product principles

- **Minimal main window:** reminder title, date/time/repeat, upcoming reminders, small pet and voice preferences, and essential settings.
- **Premium original pets:** puppy first; cat and butterfly are later characters with **species-specific movement** and personality.
- **Believable performance:** no static image sliding across the screen, paw skating, awkward snap transitions, randomly moving mouths, or endless artificial bouncing.
- **Natural offline voice:** evaluate a compatible local neural TTS voice; provide an installed Windows voice fallback. No subscription or mandatory internet connection for routine reminders.
- **Dependable scheduling:** persistent local data, resident system tray, catch-up after restart/wake/unlock, clear actions and failure recovery.
- **Respectful desktop behavior:** avoid stealing focus, blocking work, or intruding on fullscreen apps; accessibility options include reduced motion, voice off and text-only.
- **No clutter:** no pet feeding, mood meters, streaks, accounts, forced onboarding, analytics dashboards, or decorative explanations across the UI.

## Target platform and technology

| Part | Direction |
|---|---|
| Platform | Windows 10/11, desktop-first |
| Application | C# / .NET 10 / WPF |
| Pet actor | Bounded transparent desktop window, independent 2D layered artwork and animation state machine |
| Reminder engine | Local persistent scheduler in resident tray process |
| Speech | Locally generated/cached TTS, Windows voice fallback |
| Data | Offline/local per-user data, safe backups and recoverable reminders |
| Delivery | Portable Windows executable + installer after real-machine validation |
| Cost model | Free local prototype without paid cloud APIs |

No Android implementation is in scope for the initial Navin's Pet Windows milestone.

## Current project files

- [Product blueprint](docs/PRODUCT_BLUEPRINT.md)
- [Animation and character direction](docs/CHARACTER_AND_MOTION.md)
- [Complete reminder scene behavior](docs/REMINDER_PERFORMANCE.md)
- [Windows architecture](docs/ARCHITECTURE.md)
- [Development roadmap](docs/ROADMAP.md)
- [Quality / acceptance checklist](docs/QA_ACCEPTANCE.md)
- [Project status and continuity](docs/PROJECT_STATUS.md)
- [Concept 3 tail-pivot motion proof and remaining problems](docs/MOTION_PROTOTYPE_V02.md)
- [Rigid-tail animation reference implementation](tools/motion/tail_pivot_v02.py)
- [Puppy original art study and review](design/puppy-01/)

## Development phases

**1. Artwork foundation → 2. Real Windows motion proof → 3. Natural voice & response choreography → 4. Minimal reminder app integration → 5. Device QA and installer.**

**Quality gate:** do not call the pet's walking “done” until a recorded Windows test proves planted feet, natural deceleration, smooth idle/reactions and a convincing exit at normal and quarter-speed playback.

## Privacy, reliability and limitations

Routine reminders work locally without uploading reminder names. Windows cannot promise overlays/speech on the secure lock screen or while powered off; missed reminders must be recovered after resuming. Even if pet rendering or speech fails, the reminder remains accessible through a simpler fallback. We will assess licensing and distribution requirements for any third-party TTS/model dependencies before packaging.

## Ownership and scope

This repository is **the sole source of truth for Navin's Pet**. It is a **new, independent Windows project**, not a rename, fork, migration, or development branch of the earlier PetPing application. Previous prototype lessons inform quality requirements, but legacy app code and assets are **not automatically imported**. Source artwork here is original and experimental until art review.

_No public license is granted by this README. Choose an appropriate repository license before external distribution._
