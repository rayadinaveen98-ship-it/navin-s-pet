# Animation pipeline reset — 2026-10-19

**Decision status:** Direction approved by product feedback; specific paid tooling still evaluation-only. **No software purchase, professional rig, export or successful desktop animation is being claimed.**

## Why the approach changes
User explicitly rejected V04 as uneven and imperfect. Earlier V01–V03 motion attempts had rubbery tail motion, blurred reconstructed eyelids, distorted fur or cutout seams. These artifacts all rely on manipulating a **flattened** AI-generated Concept 3 character image.

Continue using the user's **approved Concept 3 design** as visual identity/reference, but stop treating the flattened image as the final animation-ready rig. Do not continue the inpainting/pixel-warp loop as the production direction. Prior exploratory animations remain research artifacts only.

## Tool evaluation based on official documentation (2026-10-19)
| Purpose | Candidate | Strength | Qualification |
|---|---|---|---|
| Layered character master | Krita (free), Photoshop or Clip Studio Paint | paint actual missing geometry and create independently editable head, eyelids, face, fur, paws, ears, tail, body | manual illustration and consistency correction are mandatory |
| Character acting, expressive rig | **Moho Pro 14**, evaluate trial first | PSD layered bitmap import, Smart Bones, IK, corrective geometry and switch drawings | paid, no automatic magic conversion from flattened picture |
| Alternative integration-focused rig | **Spine 2D** | mesh weights, 2D skeletons, IK, authored timelines, transparent PNG sequences / atlases | paid for saving/exporting; integration with WPF must be tested rather than assumed |
| Highest complexity | Toon Boom Harmony | mixed hand-drawn/rig animation, sophisticated deformers | higher cost and production complexity; not default for one small desktop mascot |
| AI image-to-video | reference-only | motion exploration and timing inspiration | consistency/art fidelity insufficient as authoritative runtime character asset |

Official references:
- Moho Pro: https://moho.lostmarble.com/en-jp/products/moho-pro-14
- Spine features: https://en.esotericsoftware.com/
- Spine export: https://us.esotericsoftware.com/spine-export/
- Krita features: https://krita.org/en/features/
- Harmony: https://www.toonboom.com/products/harmony

## Recommended prototype workflow
1. **Lock exact visual identity:** retain Concept 3 as the visible art target (silhouette, fur, collar/tag, face and proportions). New artist-created layers must be matched and approved against it.
2. **Draw a layered PSD/KRA master, don't simply cut and warp:** neutral open-eye, half-closed and closed lids, head/neck rear fill, separate ears, tail root and back fill, torso/chest, fore/hind limbs and paw contact shadows. Draw genuinely hidden material; repair all edges.
3. **Art QA:** compare reconstructed neutral pose to Concept 3 at normal size and high zoom. Reject if recognizable traits changed, joints detach or repeating texture patches appear.
4. **Trial rig in Moho:** very small **3–5 second idle proof** — two convincing blinks, eyes/head/ears and shape-preserving tail with grounded paws. Use authored art layers and corrective shapes; no global image warp. If Moho trial license limitations obstruct save/export, use screen capture solely for tool evaluation, not production assets.
5. **Second proof:** authored quadruped contact/pass/stop/turn cycle, with foot-to-world coordinates validated on desktop. Do not just drag an image horizontally.
6. **Export test:** lossless alpha PNG sequence/atlas from chosen tool into a native Windows WPF transparent overlay; measure performance, 100–200% scaling, focus avoidance, clipping and alpha edges. Avoid GIF as release format.
7. **Only then** layer in local voice playback, mouth shapes, Done/Snooze reactions and persisted reminder actions.

## Acceptance gates
- No new still pose sheet counts as animated proof.
- No new V0x version considered visually approved without reviewing actual moving footage (normal and 0.25x) **against user-locked Concept 3**.
- Preserve body and tail volume, limb lengths, face proportions, eye highlights, collar and fur edge; stop and correct visible deformations, sliding paws or unpainted holes.
- Keep artwork work isolated; no regressions of scheduling or creation of a paid dependency without consent.
- Only commit Navin's Pet code and assets to `rayadinaveen98-ship-it/navin-s-pet`.

## Near-term decision
**Preferred trial:** Krita for art preparation + Moho Pro for first authored-rig proof.  
**Alternative:** Krita + Spine if Moho output or UI development pipeline proves unsuitable.  
**Do not buy any subscription/licence yet**; a trial-quality proof is required first.

## Next deliverable
A layered-art requirements package and evidence-based tool pilot, followed by a genuine **playable rigged idle clip**, not another warped raster experiment. Confirm user budget preference before incurring any costs. 
