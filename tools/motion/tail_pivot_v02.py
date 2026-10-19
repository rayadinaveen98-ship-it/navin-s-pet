#!/usr/bin/env python3
"""Navin's Pet: Concept 3 tail-pivot animation prototype.

Uses EXACT user-supplied locked concept-sheet image as runtime input.
IMPORTANT: this is a masked 2D RIG STUDY, not the final production pet rig.
No scaling or local elastic deformation of the tail is used.

Run: python tools/motion/tail_pivot_v02.py --image path/to/approved-concept3.png --output out.mp4
Deps: numpy, opencv-python and ffmpeg on PATH.
"""
import argparse
import math
import subprocess

import cv2
import numpy as np

W, H, FPS = 690, 910, 30
SECONDS = 5.2
PIVOT = (166, 533)  # painted tail root in approved sheet, in source pixels
TAIL_ENVELOPE = np.array([
    (206,351),(181,353),(153,350),(121,359),(95,376),(65,398),
    (48,425),(28,463),(23,507),(31,548),(55,583),(82,605),
    (77,625),(94,644),(116,659),(138,649),(161,622),(166,588),
    (168,560),(188,535),(203,508),(214,482),(218,460),
    (203,434),(190,414),(169,396),(186,386),(204,372)
], dtype=np.int32)


def smoothstep(start, stop, x):
    a = np.clip((x - start) / (stop - start), 0, 1)
    return a * a * (3 - 2 * a)


def prepare(source):
    """Extract tail's approximate fur matte; retain a static foreground torso."""
    original = source.astype(np.float32)
    paper = np.median(source[:, 2:18, :], axis=1).astype(np.float32)[:, None, :]
    rr, gg, bb = original[:, :, 2], original[:, :, 1], original[:, :, 0]
    rb, gb, bb0 = paper[:, :, 2], paper[:, :, 1], paper[:, :, 0]
    delta = np.sqrt(.28 * (rr-rb)**2 + .65 * (gg-gb)**2 + .95 * (bb-bb0)**2)
    tint = (rr - .5 * (gg+bb)) - (rb - .5 * (gb+bb0))

    envelope = np.zeros((H, W), np.float32)
    cv2.fillPoly(envelope, [TAIL_ENVELOPE], 1)
    envelope = cv2.GaussianBlur(envelope, (0, 0), 1)
    tail_alpha = (smoothstep(7, 30, np.maximum(delta, 1.3*tint)) * envelope).astype(np.float32)

    # Smooth paper reconstruction beneath removed tail; torso is restored above it.
    paper = cv2.GaussianBlur(paper, (1, 51), 0)
    base = np.repeat(paper, W, axis=1)
    empty = original * (1-tail_alpha[:, :, None]) + base * tail_alpha[:, :, None]

    yy, xx = np.indices((H, W), dtype=np.float32)
    limit = np.interp(yy, [0,420,450,480,520,560,620,670,910],
                      [700,222,216,197,182,149,126,100,70])
    fur = smoothstep(9, 28, np.sqrt(((original - np.median(
        source[:,2:18,:],axis=1).astype(np.float32)[:,None,:])**2).mean(axis=2)))
    occlusion = smoothstep(-4, 9, xx-limit) * fur
    return original, empty, original * tail_alpha[:, :, None], tail_alpha, occlusion


def pose_angle(seconds):
    # Slow, intentional tail motion (zero velocity at keyframes).
    keys = [(0,0),(.85,5),(1.7,-5),(2.55,4),(3.5,-3),(4.35,1.5),(5.2,0)]
    for (t0,a0),(t1,a1) in zip(keys,keys[1:]):
        if seconds <= t1:
            s = smoothstep(0,1,(seconds-t0)/(t1-t0))
            return a0 + (a1-a0) * s
    return 0.0


def compose(layers, degrees):
    original, empty, premultiplied_tail, tail_alpha, occlusion = layers
    matrix = cv2.getRotationMatrix2D(PIVOT, degrees, 1.0)  # rigid, scale=1
    rgb = cv2.warpAffine(premultiplied_tail, matrix, (W,H),
                         flags=cv2.INTER_CUBIC, borderValue=(0,0,0))
    matte = cv2.warpAffine(tail_alpha, matrix, (W,H),
                           flags=cv2.INTER_CUBIC, borderValue=0)
    matte = np.clip(matte,0,1)[:, :, None]
    background = empty * (1-matte) + rgb
    out = background*(1-occlusion[:,:,None]) + original*occlusion[:,:,None]
    return np.uint8(np.clip(out,0,255))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image',required=True,help='Approved full Concept 3 sheet PNG')
    parser.add_argument('--output',default='tail_pivot_v02.mp4')
    args = parser.parse_args()
    sheet = cv2.imread(args.image)
    if sheet is None or sheet.shape[0] < H or sheet.shape[1] < W:
        parser.error('The original approved Concept 3 sheet (at least 690x910) is required')
    layers = prepare(sheet[:H,:W])
    command = ['ffmpeg','-hide_banner','-loglevel','error','-y',
               '-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}',
               '-r',str(FPS),'-i','-','-an','-c:v','libx264',
               '-pix_fmt','yuv420p','-crf','20',args.output]
    process = subprocess.Popen(command,stdin=subprocess.PIPE)
    for i in range(round(SECONDS*FPS)):
        process.stdin.write(compose(layers,pose_angle(i/FPS)).tobytes())
    process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError('ffmpeg could not encode animation')
    print('Rendered',args.output,round(SECONDS*FPS),'frames')


if __name__ == '__main__':
    main()
