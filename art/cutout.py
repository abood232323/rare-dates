"""
Local background removal for the Rare Dates hero art.

The generator gives us subjects on a flat light background with a soft cast
shadow. A naive luminance key would punch holes in the specular highlights on
the chocolate and the pomegranate seeds, so instead we only remove light pixels
that are CONNECTED TO THE BORDER. Interior highlights are never border
connected, so they survive intact.

Steps
  1. key light pixels (luminance above threshold)
  2. keep only the connected components that touch the image border
  3. feather the alpha edge, then erode a hair to kill the white fringe that
     comes from edge pixels being blended with the white background
  4. colour decontamination: unmultiply the residual white from edge pixels
  5. crop to the subject bounding box with a small margin

Usage:
  python cutout.py <in.png> <out.png> [--thresh 170] [--feather 1.2]
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def cutout(src, dst, thresh=95, feather=1.2, margin=0.02, chroma_max=30):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.float32)

    # 1. chroma key. The background and its cast shadow are NEUTRAL grey;
    #    the subject is saturated brown / red / green. Keying on chroma removes
    #    the shadow too, which a luminance key leaves behind as a solid blob.
    lum = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]
    chroma = a.max(axis=2) - a.min(axis=2)
    light = (chroma < chroma_max) & (lum > thresh)

    # 2. keep only border-connected light regions
    lbl, n = ndimage.label(light)
    border_ids = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
    border_ids.discard(0)
    bg = np.isin(lbl, list(border_ids)) if border_ids else np.zeros_like(light)

    # fill any pinholes inside the subject that got keyed by mistake
    subject = ndimage.binary_fill_holes(~bg)

    # 3. soften: feather only. Eroding bit chunks out of glossy rim highlights.
    subject = ndimage.binary_opening(subject, iterations=1)
    alpha = Image.fromarray((subject * 255).astype(np.uint8), "L")
    if feather > 0:
        alpha = alpha.filter(ImageFilter.GaussianBlur(feather))
    al = np.asarray(alpha).astype(np.float32) / 255.0

    # 4. decontaminate: edge pixels are subject blended over white, so
    #    unmultiply the white contribution where alpha is partial
    safe = np.clip(al, 0.25, 1.0)[..., None]
    rgb = np.clip((a - 255.0 * (1.0 - safe)) / safe, 0, 255)
    rgb = np.where(al[..., None] > 0.98, a, rgb)

    out = np.dstack([rgb, al * 255.0]).astype(np.uint8)
    img = Image.fromarray(out, "RGBA")

    # 5. crop to subject with margin
    ys, xs = np.where(al > 0.06)
    if len(xs):
        pad = int(max(img.width, img.height) * margin)
        box = (max(0, xs.min() - pad), max(0, ys.min() - pad),
               min(img.width, xs.max() + pad), min(img.height, ys.max() + pad))
        img = img.crop(box)

    img.save(dst, optimize=True)
    cov = float((al > 0.5).mean())
    print(f"{dst}  {img.width}x{img.height}  subject={cov*100:.1f}%")


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    opts = {}
    for i, x in enumerate(sys.argv):
        if x == "--thresh":
            opts["thresh"] = float(sys.argv[i + 1])
        if x == "--feather":
            opts["feather"] = float(sys.argv[i + 1])
        if x == "--chroma":
            opts["chroma_max"] = float(sys.argv[i + 1])
    cutout(args[0], args[1], **opts)
