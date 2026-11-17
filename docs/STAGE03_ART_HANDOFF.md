# Stage 03 — Concept 3 layered-art handoff and acceptance contract

**Prepared:** 17 November 2026  
**Status:** IMPLEMENTED as a specification/validation scaffold only. **NOT** approved production art, an animation, or a Windows build.  
**Scope:** first puppy only; stay in the independent \`navin-s-pet\` repository.

## Source-of-truth audit

- **Identity is locked:** the user-approved **Concept 3 puppy** is the target (silhouette, proportions, facial expression language, cream/tan fur, eyes, collar and gold tag).
- \`design/puppy-01/puppy-side-rig.svg\` is an earlier **experimental, different-looking vector study**, not an approved Concept 3 replacement.
- Earlier V02/V03/V04 preview video/GIF and original flattened source were described as conversation ZIP artifacts on 19 October. **The authoritative standalone Concept 3 source and checksum are not present in this Git repository.**
- An older concept/pose guide is a visual reference, **not an editable master and not proof that each drawn pose is anatomically consistent**.
- **Blocker:** acquire/confirm the exact user-approved high-resolution Concept 3 reference master and provenance before claiming faithful layered reconstruction. Do not silently substitute a newly generated dog or transfer private conversation assets into the public repository without reviewing rights and distribution intent.

## Layered master handoff

Editable source file: \`concept3-master.kra\` (Krita) or other genuinely editable layered document, plus its layered PSD interchange if viable. Final filenames are pending real art production.

The layer contract lives in \`design/puppy-01/concept3-rig-manifest.json\`. Required independent render parts (drawn hidden geometry, not cutout masks from a flattened sheet):

| Stack group | Required parts | What must remain true |
|---|---|---|
| Screen anchor | \`ground-shadow\` | Stays on the virtual desktop ground plane; doesn't inherit head/body transforms |
| Rear geometry | \`tail-root-fill\`, \`tail\`, \`hindleg-far\`, \`foreleg-far\` | Full tail root and concealed rear-leg edges are painted |
| Body / occlusion | \`torso\`, \`neck-backfill\`, \`hindleg-near\`, \`foreleg-near\` | Torso remains solid as head/legs move; no transparent holes or clipped fur |
| Head / ears | \`head\`, \`ear-far\`, \`ear-near\` | Stable silhouette, ears have independent pivot and painted attachment |
| Expression switches | \`eyes-open\`, \`eyes-half\`, \`eyes-closed\`, \`brow-left\`, \`brow-right\`, \`mouth-neutral\`, \`mouth-small\`, \`mouth-open\` | Custom-painted lid folds and mouth interiors; never texture-smear over pupils |
| Accessories | \`collar-tag\` | Collar/tag remain anchored and don't float or intersect cheeks |

These are the **minimum** names for a handoff: additional explicit correction/occlusion layers are welcome when actually drawn. Some parts are mutually exclusive pose switches (eyes, mouths) and **must never render simultaneously**.

### Coordinates and export
1. All exported 8-bit RGBA PNG parts use the **same exact transparent canvas and source pixel origin**, preserving alignment. Do not trim individual parts in Stage 03.
2. Every movable part has a pivot \`[x,y]\` in original source pixels; ground shadow is screen anchored.
3. Provide actual reference file and SHA-256, layer paths and pivots in the manifest; record user art-review acceptance in \`art_approval\`.
4. Run the dependency-free validator. \`structure\` checks the **unfilled contract**, while \`production\` must reject missing source, unfilled pivots, incomplete exports, absent visual sign-off and invalid PNG headers.
5. This automated check **cannot** certify anatomy, seams, edge quality, actual alpha pixels, correct expression timing, rig quality or foot planting. Human/art and Windows recording review are separate mandatory gates.

\`\`\`bash
python tools/art/validate_concept3_assets.py --mode structure
python tools/art/validate_concept3_assets.py --mode production
python -m unittest discover -s tools/art -p "test_*.py" -v
\`\`\`

## Animation deliverables and review order

**Gate A — Neutral composite:** master artwork reconstructs the locked visual appearance at normal size, close zoom and 64/120/180/240 px; front, side, 3/4 views are consistent. Check light/dark/busy wallpapers and head/tail/ear rotations.

**Gate B — Idle rig:** authentic **3–5-second** continuous 2D performance. Painted closed and half lids; 1–2 believable blinks, subtle head/ear movement, small rigid-volume-preserving tail action and correctly grounded paws. Review unsped and 0.25x video. No pixel warping, no blurred reconstructed eye texture.

**Gate C — Quadruped walking:** authored contact/passing frames for fore/hind opposite legs, stance paw anchored in world coordinates, real stride-based root translation, stop/settle and true turn/exit. Review 1.0x and 0.25x. Reject paw sliding or knee popping.

**Gate D — Native alpha overlay:** test exported sequence in a bounded, click-safe Windows WPF harness at 100–200% DPI with no focus theft, visible matte seams or unbounded CPU cost. **Do not call the app installed or the Windows pipeline proven without actual device evidence.**

## Stop rules and governance

- The user-approved *look* is not permission to switch breeds, facial geometry, costume, palette or rigging style.
- Do not infer successful animation from a static guide or an isolated prototype.
- No source/art overwrite on \`main\`, no old PetPing changes, no paid tool purchase, no merge or release without separate review.
- Next milestone is a **layered Concept 3 neutral artwork candidate plus verifiable source attribution**, not another pixel-warp V05.
