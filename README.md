# Rare Dates

Brand package and website for Rare Dates (`raredates.jo`), a Jordanian maker of
Jordan Valley Medjool filled and finished in Belgian chocolate.

## Run it

```bash
node serve.mjs                 # http://localhost:3001
```

Screenshots:

```bash
node screenshot.mjs http://localhost:3001 label            # 794px, as supplied
node screenshot-wide.mjs http://localhost:3001 label 1440  # desktop
```

Two query params exist for testing only: `?static=1` disables entrance
animations so a full-page capture is not blank below the fold, and `?lang=ar`
is reserved for the bilingual pass.

## What is here

```
index.html          The whole site. One file, Tailwind via CDN, no build step.
brand/              The brand package, and the reason the site says what it says
├── decisions.md    BINDING. Read first, it overrides everything else.
├── context.md      Brand DNA, assets worth keeping, defects on record
├── audience.md     Personas, buying behaviour, audience language
├── positioning.md  Category strategy, competitive map, proof points
├── messaging.md    Message hierarchy, taglines, WhatsApp scripts
├── voice.md        Tone, vocabulary, writing rules, Arabic register
├── identity.md     The visual system the site is built from
├── guidelines.md   Client-facing brand book
└── brand.yaml      Machine-readable manifest
art/
├── web/            The 20 optimised cutouts the site loads (1.6MB)
├── key.py          Chroma keyer: measures the screen colour per image and
│                   splits with Otsu, because screen strength varies per render
├── largest.py      Drops stray objects and attached cast shadows
├── despill_shadow.py  Removes a coloured shadow smear the keyer cannot reach
└── normalize.py    Puts every date on one canvas at one optical size
archive/            The first catalogue build, kept for reference
```

`art/raw/` and `art/cut/` are gitignored: 147MB of generation sources and
intermediates. Everything the site needs is in `art/web/`.

## The site

**Hero.** Five flavours on a kinetic carousel. Arrows, arrow keys, drag, or the
rail. Each flavour brings its own ground, bloom and accent while gold and cream
stay constant, so the stage transforms without the brand moving.

**The collection.** Six cards. Five flavours plus the weekly drop. The card
whose flavour is live in the hero sits empty, and scrolling flies that date down
into its own slot, completing the set. The path is deliberately not a straight
line, and it is near-linear in position for a reason documented in the code:
both ends of the path scroll with the page, so any easing steep enough to feel
nice makes the date swim backwards up the screen.

**The Jordan Valley.** The one claim competitors structurally cannot make.

**Flavour pages.** Hash-routed views (`#/pistachio`), so every flavour is
linkable and the back button works. The date travels from its card into the
page as one continuous object rather than two pictures cross-fading.

**Corporate and footer.** Bulk gifting, contact, allergens, shelf life.

## Configuration

One place, near the top of the script in `index.html`:

```js
const WHATSAPP = "962798781310";   // every CTA on the site points here
const PRICE    = "JOD 15";         // shown on every card and flavour page
```

## Still open

- **Arabic.** Committed in `decisions.md` D5 and not built. The toggle was
  removed rather than left dead. This is the largest remaining gap: the repeat
  customer in `audience.md` reads Arabic.
- **Box formats.** Sizes are in development, so the site sells one box at one
  price and shows no packaging it cannot yet deliver.
- **The weekly poll.** The sixth card says the audience picks the flavour. Today
  that goes to WhatsApp; when the poll exists, repoint `#nextCta`.
- **Real photography.** The product imagery is generated. `decisions.md` D2
  records that decision, the risk, and the rules the site follows because of it.
  The image slots are fixed-ratio so a real shoot drops in with no rework.
