"""
Put every date on one common canvas.

Each cutout is tightly cropped to its own subject, so an object-fit:contain box
scales each one differently: a tall date fits to the box height, a wide one fits
to the box width, and the set stops looking like a set. Worse, the hero and the
card render the same date at different relative sizes.

Fix, in two parts:
  1. scale every date so its painted AREA is equal. Area rather than bounding
     box, because these sit at different angles and a diagonal one has a much
     larger box for the same real size.
  2. paste onto one canvas whose aspect matches the display boxes exactly. When
     image aspect == box aspect, contain renders the image at exactly the box
     size, so the subject's on-screen size is predictable everywhere.

The set is auto-fitted: if equalising areas would push the tallest date past the
canvas, the whole set scales down together, which keeps areas equal.
"""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(__file__)
SRC, OUT = os.path.join(HERE, 'cut'), os.path.join(HERE, 'web')
CW, CH = 1000, 1100          # canvas, aspect 1 / 1.1  -> matches .date and .card-slot
FIT = 0.94                   # subject may use at most this much of the canvas
NAMES = ['date-pomegranate', 'date-chocolate', 'date-coffee', 'date-pistachio', 'date-lemon']


def opaque_area(im):
    return int((np.asarray(im)[..., 3] > 30).sum())


def main():
    ims = {n: Image.open(os.path.join(SRC, n + '.png')).convert('RGBA') for n in NAMES}
    areas = {n: opaque_area(im) for n, im in ims.items()}

    goal = CW * CH * 0.42                     # opening bid for subject coverage
    scales = {n: float(np.sqrt(goal / areas[n])) for n in NAMES}

    # auto-fit: shrink the whole set if any subject would overflow the canvas
    worst = max(max(ims[n].width * scales[n] / (CW * FIT),
                    ims[n].height * scales[n] / (CH * FIT)) for n in NAMES)
    if worst > 1:
        for n in NAMES:
            scales[n] /= worst
        print(f"auto-fit: whole set scaled by {1/worst:.3f} so the tallest date fits\n")

    print(f"{'date':<20}{'area':>10}{'scale':>8}   result")
    for n in NAMES:
        im, sc = ims[n], scales[n]
        w, h = max(1, round(im.width * sc)), max(1, round(im.height * sc))
        r = im.resize((w, h), Image.LANCZOS)
        canvas = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
        canvas.paste(r, ((CW - w) // 2, (CH - h) // 2), r)
        dst = os.path.join(OUT, n + '.webp')
        canvas.save(dst, 'WEBP', quality=90, method=6)
        print(f"{n:<20}{areas[n]:>10,}{sc:>8.3f}   {w}x{h} on {CW}x{CH}  "
              f"{os.path.getsize(dst)//1024}KB")

    after = [opaque_area(Image.open(os.path.join(OUT, n + '.webp')).convert('RGBA')) for n in NAMES]
    before = list(areas.values())
    print(f"\narea spread: {(max(before)-min(before))/np.mean(before)*100:.1f}%"
          f"  ->  {(max(after)-min(after))/np.mean(after)*100:.1f}%")
    print(f"subject covers {np.mean(after)/(CW*CH)*100:.0f}% of canvas "
          f"({np.sqrt(np.mean(after)/(CW*CH))*100:.0f}% linear)")


if __name__ == '__main__':
    main()
