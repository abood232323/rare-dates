"""
Remove a coloured cast-shadow smear left attached to a subject.

The general keyer cannot separate this one: the smear is joined to the subject,
is thick enough to survive an opening, and pushing the chroma-shadow term hard
enough to catch it starts biting into the subject's own rim.

It is trivially separable on colour and position though. The smear is the screen
colour darkened, and it sits below the product, where the product itself is
chocolate. So: drop screen-hued pixels inside the lowest slice of the subject.

  python despill_shadow.py in.png out.png --hue green|blue --band 0.14
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

src, dst = sys.argv[1], sys.argv[2]
hue = "green"
band = 0.14
for i, x in enumerate(sys.argv):
    if x == "--hue":  hue = sys.argv[i + 1]
    if x == "--band": band = float(sys.argv[i + 1])

im = Image.open(src).convert("RGBA")
a = np.asarray(im).astype(int).copy()
al = a[..., 3]
rgb = a[..., :3]
m = al > 40
ys, _ = np.where(m)
lo, hi = ys.min(), ys.max()
floor = hi - (hi - lo) * band

if hue == "green":
    hued = (rgb[..., 1] > rgb[..., 0] + 14) & (rgb[..., 1] > rgb[..., 2] + 14)
else:
    hued = (rgb[..., 2] > rgb[..., 0] + 14) & (rgb[..., 2] > rgb[..., 1] + 14)

rows = np.arange(a.shape[0])[:, None]
kill = m & hued & (rows > floor)
kill = ndimage.binary_dilation(kill, iterations=2)      # take the soft halo too
al2 = np.where(kill, 0, al).astype(np.uint8)

# feather the new boundary so it does not read as a cut
sm = np.asarray(Image.fromarray(al2, "L").filter(ImageFilter.GaussianBlur(1.2)))
a[..., 3] = np.minimum(al2, sm) if False else sm
a[..., 3] = np.where(kill, 0, a[..., 3])

ys2, xs2 = np.where(a[..., 3] > 25)
pad = int(max(im.size) * 0.02)
out = Image.fromarray(a.astype(np.uint8), "RGBA").crop(
    (max(0, xs2.min() - pad), max(0, ys2.min() - pad),
     min(im.width, xs2.max() + pad), min(im.height, ys2.max() + pad)))
out.save(dst)
print(f"  removed {int(kill.sum()):,}px of {hue} shadow -> {out.width}x{out.height}")
