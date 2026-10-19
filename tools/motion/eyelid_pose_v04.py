#!/usr/bin/env python3
"""Navin's Pet — V04 textured eyelid pose tool (art study only).

The user's locked Concept 3 sheet is still a FLAT image. This produces
temporary blink poses by masking original eyes and copying nearby painted fur;
it is NOT a professionally separated eyelid or final character rig.

Run:
  pip install opencv-python numpy
  python tools/motion/eyelid_pose_v04.py --image approved-concept3.png --output poses/
"""
from pathlib import Path
import argparse
import math
import cv2
import numpy as np

WIDTH, HEIGHT = 690, 910
# Original locked Concept 3 art coordinates: eye centers, approximate ellipse,
# location of comparable fur sample. Do not reuse for other puppies.
EYES = [
    (405, 268, 39, 42, 35, 103, 10),
    (530, 200, 40, 43, 26, 91, -13),
]


def smoothstep(start, end, value):
    u = np.clip((value - start) / (end - start), 0, 1)
    return u * u * (3 - 2 * u)


def prepare(img):
    """Cache fur texture and lid geometry before any frame rendering."""
    yy, xx = np.indices((HEIGHT, WIDTH), dtype=np.float32)
    result = []
    for cx, cy, rx, ry, shiftx, shifty, deg in EYES:
        skin = cv2.warpAffine(
            img, np.float32([[1, 0, shiftx], [0, 1, shifty]]),
            (WIDTH, HEIGHT), flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_REFLECT_101,
        ).astype(np.float32)
        theta = math.radians(deg)
        u = ((xx-cx)*math.cos(theta)+(yy-cy)*math.sin(theta))/rx
        v = (-(xx-cx)*math.sin(theta)+(yy-cy)*math.cos(theta))/ry
        ell = u*u + v*v
        edge = smoothstep(0, 1, np.clip((1.08-ell)*ry/4.1, 0, 1))
        result.append((skin, u, v, edge, (cx, cy, rx, ry, deg)))
    return result


def make_pose(original, layers, closure):
    """Render 0=open, 0.5=half-lid, 1=closed. No eyeball scaling."""
    if closure < .001:
        return original.copy()
    result = original.astype(np.float32).copy()
    for skin, u, v, edge_mask, (cx,cy,rx,ry,deg) in layers:
        front = -1.13 + 2.39*closure + .08*u*u - .03*u
        travel = np.clip((front-v)*ry/2.7+.5, 0, 1)
        a = (travel*edge_mask)[:, :, None]
        result = result*(1-a) + skin*a
        if closure > .78:
            amount = float(smoothstep(.78, 1., closure))
            theta = math.radians(deg)
            points = []
            for uu in np.linspace(-.69,.69,31):
                vv = .16 + .15*uu*uu - .045*uu
                px = cx + rx*uu*math.cos(theta)-ry*vv*math.sin(theta)
                py = cy + rx*uu*math.sin(theta)+ry*vv*math.cos(theta)
                points.append([round(px),round(py)])
            overlay = np.uint8(np.clip(result,0,255)).copy()
            # 1px warm cocoa crease; not a gray hand-drawn marker.
            cv2.polylines(overlay,[np.array(points,np.int32)],False,
                          (69,98,143),1,cv2.LINE_AA)
            result = result*(1-.75*amount)+overlay.astype(np.float32)*(.75*amount)
    return np.uint8(np.clip(result, 0, 255))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--image', required=True, help='User-locked full Concept 3 character sheet')
    ap.add_argument('--output', default='eyelid-poses-v04')
    args = ap.parse_args()
    original = cv2.imread(args.image)
    if original is None or original.shape[0] < HEIGHT or original.shape[1] < WIDTH:
        ap.error('Expected locked Concept 3 source, at least 690x910')
    original=original[:HEIGHT, :WIDTH]
    out=Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    prepared=prepare(original)
    for name, value in [('open',0),('half',.53),('closed',1)]:
        if not cv2.imwrite(str(out/(name+'.png')),make_pose(original,prepared,value)):
            raise OSError('Could not save '+name)
    print('Three art-study eyelid poses saved to', out)


if __name__ == '__main__':
    main()
