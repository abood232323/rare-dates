"""
Chroma-key cutout for the Rare Dates art.

Why colour-distance and not a channel difference:
the first version keyed on `G - max(R,B)` (or the blue equivalent) against one
fixed threshold. Two things went wrong.

  1. Screen strength varies per generation. Measured across the five dates, the
     background score started as low as 46 on one image and as high as 101 on
     another, while a shadowed subject reached 80. No single threshold fits.
  2. Shadowed parts of a subject pick up screen bounce, so their score climbs
     toward the background's and they get keyed away. That is what tore holes
     in the pistachio date and notched the others.

This version measures the actual screen colour from the border, keys on
distance from it, and finds the split per image with Otsu. A shadowed subject
pixel carrying spill is still far from the screen colour because it is much
darker, so it survives, while the flat screen does not.
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def otsu(v, bins=256):
    """Split a 1D distribution into two clusters. Standard Otsu."""
    hist, edges = np.histogram(v, bins=bins)
    hist = hist.astype(float)
    w = np.cumsum(hist)
    total = w[-1]
    if total == 0:
        return float(np.median(v))
    centres = (edges[:-1] + edges[1:]) / 2
    s = np.cumsum(hist * centres)
    w0 = w
    w1 = total - w0
    valid = (w0 > 0) & (w1 > 0)
    m0 = np.divide(s, w0, out=np.zeros_like(s), where=w0 > 0)
    m1 = np.divide(s[-1] - s, w1, out=np.zeros_like(s), where=w1 > 0)
    between = w0 * w1 * (m0 - m1) ** 2
    between[~valid] = -1
    return float(centres[int(np.argmax(between))])


def key(src, dst, screen="green", feather=1.0, margin=0.02, band=0.28, shadow=0.45, edge=4):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    h, w, _ = a.shape

    # 1. what colour is the screen, actually? measure it rather than assume
    ring = np.zeros((h, w), bool)
    ring[:8] = ring[-8:] = True
    ring[:, :8] = ring[:, -8:] = True
    screen_rgb = np.median(a[ring], axis=0)

    # 2. distance from that colour
    dist = np.sqrt(((a - screen_rgb) ** 2).sum(axis=2))

    # A cast shadow is the screen colour darkened, so it sits far away in plain
    # RGB distance and survives the key as a smear stuck to the subject. It does
    # however keep the screen's CHROMATICITY. Measure that separately and treat
    # anything matching the screen's hue but darker than it as background too.
    tot = a.sum(axis=2, keepdims=True) + 1e-6
    chrom = a / tot
    screen_chrom = screen_rgb / (screen_rgb.sum() + 1e-6)
    cdist = np.sqrt(((chrom - screen_chrom) ** 2).sum(axis=2)) * 441.67
    lum = a.mean(axis=2)
    ct = otsu(cdist[::3, ::3].ravel()) * shadow
    shadowish = (cdist < ct) & (lum < screen_rgb.mean() * 0.97)

    # 3. split per image. Otsu on a subsample keeps it quick and stable.
    t = otsu(dist[::3, ::3].ravel())
    t0, t1 = t * (1 - band), t * (1 + band)     # narrow ramp around the split

    # 4. background is flat screen AND reachable from the border, so a genuinely
    #    screen-coloured detail inside the subject is never punched out
    lbl, _ = ndimage.label((dist < t) | shadowish)
    ids = set(lbl[0, :]) | set(lbl[-1, :]) | set(lbl[:, 0]) | set(lbl[:, -1])
    ids.discard(0)
    bg = np.isin(lbl, list(ids)) if ids else ((dist < t) | shadowish)
    subject = ndimage.binary_fill_holes(~bg)

    # 5. soft matte only across the boundary band; interiors stay fully opaque.
    #    No opening or erosion here: both bit chunks out of glossy rims.
    # NOTE: shadowish deliberately does NOT zero the ramp directly. A subject can
    # legitimately match the screen's hue (the pistachio date's skin is purple
    # from blue spill). It only feeds the border-connected background test above,
    # so an interior match survives while a shadow joined to the screen does not.
    # The ramp belongs at the BOUNDARY only. Applied across the whole subject it
    # punched holes in glossy highlights: a bright specular on the chocolate sits
    # close to a light screen in RGB distance, so it read as half background.
    # Coffee's screen was the lightest of the set and showed it worst. Anything
    # inset from the edge is solid by definition, whatever colour it happens to be.
    interior = ndimage.binary_erosion(subject, iterations=edge)
    ramp = np.clip((dist - t0) / max(t1 - t0, 1e-6), 0.0, 1.0)
    ramp = np.where(interior, 1.0, ramp)
    al = np.where(subject, ramp, 0.0).astype(np.float32)

    alpha = Image.fromarray((al * 255).astype(np.uint8), "L")
    if feather > 0:
        alpha = alpha.filter(ImageFilter.GaussianBlur(feather))
    al = np.asarray(alpha).astype(np.float32) / 255.0

    # 6. spill suppression: pull the screen channel back toward its neighbours
    out = a.copy()
    if screen == "green":
        # Capping against max(R,B) was too gentle: a dark brown rim pixel keeps
        # more green than it should and the whole edge reads olive, which looks
        # like mould on chocolate. Cap against the MEAN instead, matching the
        # blue treatment. Safe here because nothing shot on green is green.
        out[..., 1] = np.minimum(a[..., 1], (a[..., 0] + a[..., 2]) * 0.5 * 1.02)
    else:
        out[..., 2] = np.minimum(a[..., 2], (a[..., 0] + a[..., 1]) * 0.5 * 1.02)

    rgba = np.dstack([np.clip(out, 0, 255), al * 255.0]).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")

    ys, xs = np.where(al > 0.06)
    if len(xs):
        pad = int(max(img.width, img.height) * margin)
        img = img.crop((max(0, xs.min() - pad), max(0, ys.min() - pad),
                        min(img.width, xs.max() + pad), min(img.height, ys.max() + pad)))
    img.save(dst, optimize=True)

    holes = int((ndimage.binary_fill_holes(al > .25) & (al <= .25)).sum())
    print(f"{dst:<34} {img.width}x{img.height}  screen rgb "
          f"{tuple(int(c) for c in screen_rgb)}  split {t:5.1f}  holes {holes}")


if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    o = {}
    for i, x in enumerate(sys.argv):
        if x == "--screen":
            o["screen"] = sys.argv[i + 1]
        if x == "--feather":
            o["feather"] = float(sys.argv[i + 1])
        if x == "--band":
            o["band"] = float(sys.argv[i + 1])
        if x == "--shadow":
            o["shadow"] = float(sys.argv[i + 1])
        if x == "--edge":
            o["edge"] = int(sys.argv[i + 1])
    key(args[0], args[1], **o)
