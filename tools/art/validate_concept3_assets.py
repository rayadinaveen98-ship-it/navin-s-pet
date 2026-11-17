#!/usr/bin/env python3
"""Validate the Concept 3 layered-art handoff manifest. Not a visual-quality test.

Usage:
  python tools/art/validate_concept3_assets.py --mode structure
  python tools/art/validate_concept3_assets.py --mode production
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys

SCHEMA = "navins-pet/concept3-rig-assets/v1"
REQUIRED = {
    "ground-shadow", "tail-root-fill", "tail", "hindleg-far",
    "foreleg-far", "torso", "neck-backfill", "hindleg-near",
    "foreleg-near", "head", "ear-far", "ear-near",
    "eyes-open", "eyes-half", "eyes-closed", "brow-left",
    "brow-right", "mouth-neutral", "mouth-small", "mouth-open",
    "collar-tag",
}
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


class ValidationError(ValueError):
    """An art handoff contract or asset requirement was not met."""


def safe_file(root: Path, value: str, field: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field}: expected nonempty relative filename")
    rel = Path(value)
    if rel.is_absolute() or any(x in ("..", ".") for x in rel.parts):
        raise ValidationError(f"{field}: path must stay within the art folder")
    resolved_root = root.resolve()
    path = (resolved_root / rel).resolve()
    if not path.is_relative_to(resolved_root):
        raise ValidationError(f"{field}: path escapes art folder")
    return path


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as fh:
        header = fh.read(26)
    if len(header) != 26 or header[:8] != PNG_MAGIC or header[12:16] != b"IHDR":
        raise ValidationError(f"{path.name}: invalid PNG header")
    width, height = struct.unpack(">II", header[16:24])
    bit_depth, colour_type = header[24], header[25]
    if width <= 0 or height <= 0 or bit_depth != 8 or colour_type != 6:
        raise ValidationError(f"{path.name}: expected nonzero 8-bit RGBA PNG")
    return width, height


def validate(data: dict, root: Path, mode: str) -> list[str]:
    if mode not in ("structure", "production"):
        raise ValidationError("mode must be structure or production")
    errors = []
    if data.get("schema") != SCHEMA or data.get("character_id") != "puppy-concept3":
        errors.append("Unexpected schema or character_id")
    layers = data.get("layers")
    if not isinstance(layers, list):
        return errors + ["layers must be a list"]
    ids = [layer.get("id") for layer in layers if isinstance(layer, dict)]
    if len(ids) != len(layers) or len(ids) != len(set(ids)):
        errors.append("Layer records must be objects with unique ids")
    missing = REQUIRED - set(ids)
    if missing:
        errors.append("Missing required layers: " + ", ".join(sorted(missing)))
    canvas = data.get("canvas", {})
    width, height = canvas.get("width"), canvas.get("height")
    dims = (width, height)
    if mode == "production" and not all(type(n) is int and 1 <= n <= 8192 for n in dims):
        errors.append("Production canvas width and height must be integers 1..8192")
    used_files = []
    for layer in layers:
        if not isinstance(layer, dict):
            continue
        layer_id = str(layer.get("id"))
        file_name = layer.get("file")
        pivot = layer.get("pivot")
        if mode == "production" and (
            not isinstance(pivot, list) or len(pivot) != 2 or
            not all(type(v) in (int, float) and v >= 0 for v in pivot)
        ):
            errors.append(f"{layer_id}: pivot [x,y] required")
        if file_name is None:
            if mode == "production":
                errors.append(f"{layer_id}: exported PNG missing")
            continue
        try:
            path = safe_file(root, file_name, f"{layer_id}.file")
            used_files.append(str(path))
            if mode == "production":
                if not path.is_file():
                    errors.append(f"{layer_id}: asset does not exist: {file_name}")
                elif path.suffix.lower() != ".png":
                    errors.append(f"{layer_id}: asset must be PNG")
                elif all(type(n) is int and 1 <= n <= 8192 for n in dims):
                    if png_dimensions(path) != dims:
                        errors.append(f"{layer_id}: PNG does not match common canvas")
        except (ValidationError, OSError) as exc:
            errors.append(str(exc))
    if len(used_files) != len(set(used_files)):
        errors.append("Different layers may not reference the same image file")
    if mode == "production":
        reference = data.get("reference", {})
        ref_file, ref_sha = reference.get("source_file"), reference.get("sha256")
        if not isinstance(ref_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", ref_sha):
            errors.append("Reference SHA-256 missing or invalid")
        if ref_file is None:
            errors.append("Approved Concept 3 master reference file missing")
        else:
            try:
                ref_path = safe_file(root, ref_file, "reference.source_file")
                if not ref_path.is_file():
                    errors.append("Reference file does not exist")
                elif isinstance(ref_sha, str) and re.fullmatch(r"[0-9a-f]{64}", ref_sha):
                    if hashlib.sha256(ref_path.read_bytes()).hexdigest() != ref_sha:
                        errors.append("Reference SHA-256 mismatch")
            except (ValidationError, OSError) as exc:
                errors.append(str(exc))
        approval = data.get("art_approval", {})
        if approval.get("layered_master_approved") is not True or not approval.get("review_evidence"):
            errors.append("Layered master requires recorded visual acceptance evidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("structure", "production"), default="structure")
    parser.add_argument(
        "--manifest", type=Path,
        default=Path(__file__).resolve().parents[2] / "design/puppy-01/concept3-rig-manifest.json"
    )
    args = parser.parse_args()
    manifest = args.manifest.resolve()
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        errors = validate(data, manifest.parent, args.mode)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {args.mode} contract only. This does NOT certify visual animation quality.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
