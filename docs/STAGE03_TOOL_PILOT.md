# Stage 03 — Animation tool pilot / decision record

**Verified:** 17 November 2026. **Decision:** no paid dependency approved; validate a free technical path before spending.  
**State:** RESEARCHED and PLANNED; no tool installed/run as part of this PR; no rigging or PNG export claimed.

## Why this is a correction to the prior plan

The previous October reset recommended a **Moho Pro trial** as the first rig test. The official trial limitations mean it **cannot import any external files (including our layered character artwork) and cannot export animations**. Therefore it cannot validate an actual Concept 3 import-to-WPF-export pipeline; it's suitable only for exploring interface, rig behaviors on internally drawn demo art and artistic ergonomics.

The **Spine trial** also disables saving and exporting, so it likewise cannot be used for a reproducible, shippable pipeline proof.

**Sources checked:**
- Moho official trial limitations: https://moho.lostmarble.com/en-jp/pages/try
- Moho installer status (14.5.1 listed 16 Nov 2026): https://moho.lostmarble.com/pages/download-moho-14
- Spine representative company forum explanation: https://us.esotericsoftware.com/forum/d/28813-saveexport-file-from-trial-version-to-pro-version/4
- Krita PNG alpha support: https://docs.krita.org/en/general_concepts/file_formats/file_png.html
- Blender stable image-sequence output guidance: https://docs.blender.org/manual/en/latest/render/output/animation.html
- Spine production PNG sequence export documentation: https://esotericsoftware.com/spine-export

## Candidate workflow, ranked by feasibility before cost

| Route | Cost now | Can the trial prove end-to-end export? | Stage 03 use |
|---|---|---|---|
| **Krita + Blender (free)** | No license purchase | Potentially yes, subject to our own actual test | Preferred first **technical** import/rig/PNG sequence experiment |
| Krita + Moho Pro trial | Trial is free, product paid later | **No**: external import and animation export disabled in trial | Evaluate ergonomics only. Paid tool needs separate approval |
| Krita + Spine trial | Trial free, product paid later | **No**: saving/export disabled in trial | Evaluate workflow only; no future source persistence |
| Krita only + authored frame sequence | No license purchase | Potentially yes | Fallback for hand-authored blink/idle if rig tools underperform |

Blender's documented frame-sequence rendering supports lossless PNG output, but this **does not prove** the rigged puppy, WPF transparency, visual quality, CPU load or true alpha exports. The selected art/render workflow is still provisional.

## Evidence-based free technical pilot

1. **Inventory:** retain locked Concept 3 visuals. Do not upload unrelated personal files to public GitHub. Establish authoritative master and SHA-256; the current repository has only a different draft SVG study and empty handoff manifest.
2. **Drawn-layer proof:** make a simple explicitly disposable multi-part object/placeholder in Krita (not a claim to be the real puppy), with named layers, hidden rear fills and independent pivots.
3. **Blender import and rig:** arrange independent geometry/sprites in an orthographic camera with one grounded contact, a small lid/switch pose and a tail rotation; test draw order and silhouette stability. Record tool/version assumptions.
4. **Transparency output:** export a short 8-bit RGBA PNG sequence over transparent film on a fixed canvas, then inspect over bright/dark/checkerboard backgrounds.
5. **Playback:** exercise the sequence in a bounded Windows WPF transparent overlay **only when Phase 2 begins**. Measure display scale, focus safety, frame pacing and clipping. No invisible fullscreen click shield.
6. **Visual comparison:** once the exact approved Concept 3 original is available, recreate the **real** independent character parts with proper painted overlap and review neutral composite against it. Do not use the synthetic technical test as an art approval shortcut.
7. **Go/no-go:** if free path cannot meet performance and art gates, present actual proof, paid options and costs for separate approval. Do not silently purchase Moho, Spine or other licenses.

## Acceptance evidence ledger

| Check | Status as of 17 Nov 2026 | Required evidence |
|---|---|---|
| Exact locked reference source in repository | **BLOCKED** | User-confirmed master or approved private art-access path, checksum |
| Layer contract + missing-art fail gate | **IN PROGRESS** | Manifest, validator and local test record |
| Editable authored layered master | **NOT STARTED** | Layered KRA/PSD source and neutral recomposition |
| Krita-to-Blender technical import | **NOT RUN** | Actual tool capture/project file |
| Transparent PNG sequence | **NOT RUN** | Inspectable output PNGs, alpha check |
| Genuine rigged idle video | **NOT STARTED** | 3–5s clip at 1x and 0.25x |
| Real Windows overlay | **NOT STARTED** | WPF screenshot/recording and measurements |

### Explicit non-goals
No reminder engine changes, Windows app claims, PetPing migrations, paid-tool purchases, asset licensing shortcuts, animated GIF as shipping format, forced rebrand or desktop installer at this stage.
