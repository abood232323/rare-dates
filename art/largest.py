"""
Keep only the real subject in an RGBA cutout.

Two things this removes:

  1. Separate stray objects. The generator kept returning two dates for lemon
     however the prompt was worded, so dropping the extra one here is cheaper
     and more reliable than paying for rerolls.

  2. Wispy cast shadow still ATTACHED to the subject by a thin neck. Keeping the
     largest connected blob cannot help there, because the shadow is part of the
     same blob. Instead erode until thin necks snap, keep the core that survives,
     then grow that core back out inside the original silhouette
     (geodesic reconstruction). The subject's true edge is preserved exactly
     while anything reachable only through a thin neck is dropped.

Usage: python largest.py <in.png> <out.png> [--erode 8]
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage


def clean(src, dst, erode=8, margin=0.02, open_r=0):
    im = Image.open(src).convert("RGBA")
    a = np.asarray(im).copy()
    mask = a[..., 3] > 60
    if not mask.any():
        im.save(dst)
        return

    # Morphological opening first, when asked. A cast shadow left attached to
    # the subject is a THIN protrusion; the subject is thick. Opening at a
    # radius between the two removes the protrusion and leaves the silhouette,
    # which reconstruction cannot do because the shadow is connected.
    if open_r:
        opened = ndimage.binary_opening(mask, iterations=open_r)
        if opened.any():
            mask = mask & ndimage.binary_dilation(opened, iterations=2)

    core = ndimage.binary_erosion(mask, iterations=erode)
    if not core.any():                       # subject thinner than the erosion
        core = mask

    lbl, n = ndimage.label(core)
    if n > 1:
        sizes = ndimage.sum(core, lbl, range(1, n + 1))
        core = lbl == (int(np.argmax(sizes)) + 1)

    # grow the surviving core back out, but only within the original silhouette
    keep = ndimage.binary_propagation(core, mask=mask)
    keep = ndimage.binary_closing(keep, iterations=2)

    # Faint leftovers: a partly-keyed cast shadow can sit BELOW the mask
    # threshold entirely, so it is neither a large blob nor attached by a neck.
    # It is distinguishable by having no solid core: drop any faint region that
    # contains no fully opaque pixel.
    faint = a[..., 3] > 12
    solid = a[..., 3] > 217
    flbl, fn = ndimage.label(faint)
    if fn:
        has_core = np.zeros(fn + 1, bool)
        has_core[np.unique(flbl[solid])] = True
        has_core[0] = False
        faint_keep = has_core[flbl]
    else:
        faint_keep = faint
    keep = keep | (faint & faint_keep & ndimage.binary_propagation(keep, mask=faint))

    dropped = int((a[..., 3] > 12).sum() - keep.sum())
    a[..., 3] = np.where(keep, a[..., 3], 0)

    ys, xs = np.where(a[..., 3] > 25)
    pad = int(max(im.size) * margin)
    out = Image.fromarray(a, "RGBA").crop(
        (max(0, xs.min() - pad), max(0, ys.min() - pad),
         min(im.width, xs.max() + pad), min(im.height, ys.max() + pad)))
    out.save(dst)
    print(f"  {dst:<30} {out.width}x{out.height}  aspect 1:{out.height/out.width:.2f}"
          f"  dropped {dropped:,}px")


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    o = {}
    for i, x in enumerate(sys.argv):
        if x == "--erode":
            o["erode"] = int(sys.argv[i + 1])
        if x == "--open":
            o["open_r"] = int(sys.argv[i + 1])
    clean(args[0], args[1], **o)
