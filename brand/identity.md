# Visual Identity Brief — Rare Dates

Reads `positioning.md` · `voice.md` · `decisions.md` · `assets/source-evidence.md`.
Written for a designer who has not seen the brand. Every value here is production-ready — the
website build reads this file directly as its design system.

---

## 01 — Identity Strategy Statement

Rare Dates sits in the empty quadrant of the Jordanian gift market: modern, statement-making,
and local — between heritage houses that cannot modernise and imported luxuries that cannot be
local. The identity has to hold both halves at once, and the way it does that is **inscription**:
letterforms that look carved rather than drawn, set in deep wine and gold, with far more empty
space than a food brand is normally allowed. Nothing is illustrated, nothing is ornamented, and
nothing shines — the brand is not trying to look expensive, it is trying to look **certain**.
The restraint is not a style choice; it is the nine-piece range expressed visually, and it is the
one luxury signal that costs nothing and cannot be faked.

---

## 02 — Logo Direction

**Per D1, the identity is Mark B.** Mark A — the palm tree and ornamental script in a burgundy
circle — is retired and must be pulled from the Instagram avatar and the carousel watermark. This
section systematises Mark B rather than replacing it.

**Primary direction:** symbol + wordmark, stacked. A gold line-drawn vesica (the date-fruit /
almond form, two arcs meeting at a point top and bottom) above **RARE DATES** in letterspaced
Roman capitals.

**Character:** carved, still, and unhurried. It should read as something stamped into a box lid,
not printed on a label. It is a seal, not a signature.

**Style notes**
- **Constructed, not hand-drawn.** The vesica is two true arcs, symmetrical on both axes.
- **Single stroke weight**, optically corrected — roughly 1.5–2% of the mark's height. It must not
  thin to invisibility at small sizes.
- **The interior vertical line stays.** It is what turns a generic vesica into a date stone, and
  it is the only representational element in the entire identity.
- **Letterspacing on the wordmark: 0.18em–0.22em.** Wide, even, with the tracking visibly opened
  after `R`, `A`, `T`. Optical, not metric.
- **The mark must survive at 16px** — favicon, Instagram avatar, an embossed foil stamp. Test
  there first, not at hero size.

**What to avoid**
- Gold *gradients*, bevels, drop shadows, metallic sheen, or lens flare. Flat gold only. Foil is a
  print finish, never a screen effect — faking it is the single most common way luxury food brands
  look cheap.
- Palm trees, camels, crescents, desert dunes, Arabesque lattice, oud bottles. The entire visual
  vocabulary of Gulf-luxury cosplay — which per `positioning.md` §06 trades away the only thing
  Bateel cannot copy.
- Script, calligraphic, or handwritten Latin type anywhere near the mark.
- Enclosing the full lockup in a circle or badge. That was Mark A's move, and it is what made the
  mark collapse at small sizes.

**Lockup system — four, and only four**
| Lockup | Composition | Use |
|---|---|---|
| **Primary** | Vesica above wordmark, stacked, centred | Hero, packaging lid, anything with room |
| **Horizontal** | Vesica left, wordmark right, optically centred | Site header, email signature, letterhead |
| **Mark only** | Vesica alone | Favicon, avatar, embossing, a repeating pattern |
| **Bilingual** | Vesica above, `RARE DATES` and «تمور نادرة» stacked, hairline rule between | Packaging, Arabic site, anything customer-facing in Jordan |

**Clear space:** the height of the vesica on all four sides. **Minimum sizes:** primary lockup
28mm / 120px wide; mark only 8mm / 16px.

**Three references, and exactly what to take from each**
1. **Aesop** — take the *nerve to let a plain wordmark carry the entire brand.* No symbol
   needed, no gradient, no decoration; the confidence is the design. Take the restraint; ignore
   the apothecary palette.
2. **Diptyque** — take *the oval as a seal*: how a single containing outline, used consistently
   at every scale, becomes more recognisable than any illustration. This is the closest existing
   analogue to what the vesica should become. Ignore the dense interior lettering.
3. **Bateel** — take *the serif confidence* that sets the category ceiling and proves a date
   brand can be a luxury brand. Explicitly reject its gold-leaf ornamentation and Gulf formality
   — that is precisely the territory Rare Dates must not enter.

---

## 03 — Colour Palette

Derived from the existing Instagram assets. The palette is already correct — it has never been
documented, which is why it drifts. These are now the values.

### Wine — the primary
The brand's ground. Everything sits on it.

| Token | Hex | Role |
|---|---|---|
| `wine-900` | `#170509` | Deepest — vignette edges, gradient falloff |
| `wine-800` | `#2B0812` | Section grounds, cards on dark |
| `wine-700` | **`#4A0E1F`** | **PRIMARY.** The brand colour. Default ground. |
| `wine-600` | `#5C1327` | Elevated surfaces, hover states |
| `wine-500` | `#74192F` | Borders, dividers, active states |

Deep, warm, blood-and-oxblood rather than purple. It reads as velvet and as the inside of a date
at the same time — warmer and far more distinctive than the black-and-gold every luxury food
brand defaults to. **Never lighten it into burgundy-pink; never cool it toward aubergine.**

### Gold — the accent
| Token | Hex | Role |
|---|---|---|
| `gold-600` | `#9A7B1C` | Pressed states, gold on light grounds |
| `gold-500` | **`#C9A227`** | **PRIMARY GOLD.** The mark, headings, rules. |
| `gold-400` | `#E0C25C` | Hover, highlight, small emphasis |

`#C9A227` is antique and slightly green-shifted — brass, not costume jewellery. It is deliberately
*not* `#D4AF37`, the default "gold" that reads synthetic on screen.

### Neutrals
| Token | Hex | Role |
|---|---|---|
| `ink` | `#0D0709` | Near-black, warm-shifted. Mark B's field. Never pure `#000`. |
| `cream` | `#F2E9DC` | **All body text on dark grounds.** |
| `cream-muted` | `#B8A894` | Secondary text, captions, labels |
| `paper` | `#FAF6F0` | The one light ground, for long-form reading |

### Palette type
Monochromatic wine with a single metallic complement. Two hues, total. **The discipline is the
point — no third colour is ever introduced.** Flavour differentiation happens through photography
and typography, never by giving each product its own colour. That restraint is what makes nine
products look like one collection.

### Usage rules
- **Dark by default.** Wine or ink grounds, cream text. `paper` appears only on the story page.
- **Gold is punctuation.** The mark, headings, hairline rules, and one CTA per screen. If more
  than roughly 10% of a screen is gold, it has become decoration and must be cut back.
- ⚠️ **Accessibility:** `gold-500` on `wine-700` measures roughly 4.3:1 — acceptable for headings
  at 24px+ and for the mark, **but it fails for body text.** Body copy is always `cream` on wine
  (≈13:1). This rule is not negotiable, and it is the most likely thing to get broken in a rush.
- **Never** gold text on gold, cream on `gold-400`, or pure white anywhere — white is colder than
  this brand and instantly makes the wine look purple.

### Depth and texture — mandatory, not optional
- **Layered radial gradients, never a flat fill.** A ground is built from two or three offset
  radial gradients over the base wine — typically a warmer `#5C1327` bloom at ~30% 20% and a
  `#170509` falloff at the corners. Flat wine looks like a cheap PowerPoint template; a bloom
  looks like light falling on velvet.
- **Grain over everything.** An SVG `feTurbulence` noise layer at 3–5% opacity across full-bleed
  dark sections. It is what stops large dark areas from banding, and it does more for perceived
  quality than any other single effect.
- **Shadows are wine-tinted, layered, and low-opacity.** Never neutral grey, never a single
  `shadow-md`. Reference value:
  `0 1px 2px rgba(23,5,9,.4), 0 8px 24px rgba(23,5,9,.35), 0 24px 64px rgba(23,5,9,.25)`
- **Elevation is a three-step system:** base ground → elevated surface (`wine-800`, hairline
  `wine-500` border at 40%) → floating (adds the full shadow stack). Nothing sits at an
  undeclared level.

---

## 04 — Typography

All faces are on Google Fonts — free, licensed for commercial use, and web-ready.

### Latin

**Display / wordmark — Cinzel**
Trajan-derived Roman capitals, based on letters carved into stone rather than written with a pen.
It is what the current Mark B already approximates, so this is a formalisation, not a change. Caps
only, always. Wordmark tracking `0.20em`; display headings `0.06em`.

**Headline — Cormorant Garamond**
High-contrast old-style serif — fine hairlines, generous counters, exceptional at large sizes. It
carries the restraint and warmth Cinzel is too formal to provide, and it is the reason the brand
will not look like a law firm. Weight 300–400 only; never bold. Tracking `-0.03em` at 40px+ and
tighter as size increases. Line-height `1.1`.

> **Deliberately not Playfair Display.** It is the default "elegant serif" of every template on the
> internet, and using it would put the brand in the exact templated-luxury bucket it is trying to
> escape. Cormorant is finer, older, and has almost none of that association.

**Body / UI — Jost**
Geometric sans in the Futura lineage: circular bowls, single-storey `a`, quietly modernist. It
holds the *modern* half of the positioning while Cormorant holds the *considered* half — which is
precisely the tension the brand is built on. Weights 300/400/500. Line-height `1.7`, tracking
`0.01em`. Small labels and prices in 500 at `0.14em` tracking, uppercase.

### Arabic

**Display / wordmark — Reem Kufi**
Geometric Kufic, derived from letters **carved in stone** — the same origin as Trajan capitals.
That shared inscriptional root is why this pairing works: the Latin and Arabic marks are not
matched by shape, they are matched by *how they were made*. This is the strongest available answer
to bilingual lockup, and it is what stops «تمور نادرة» from looking like an afterthought bolted
onto a Latin logo.

**Body — Tajawal**
Modern geometric Arabic sans with the same circular construction logic as Jost. Weights 300/400/500.

### Hierarchy

| Level | Face | Size (desktop) | Weight | Tracking | Line-height |
|---|---|---|---|---|---|
| Wordmark | Cinzel | contextual | 400 | `0.20em` | 1 |
| Display / hero | Cormorant Garamond | 64–88px | 300 | `-0.03em` | 1.05 |
| Section heading | Cormorant Garamond | 36–44px | 400 | `-0.02em` | 1.15 |
| Product name | Cinzel | 18–22px | 400 | `0.10em` | 1.3 |
| Body | Jost | 16–18px | 300 | `0.01em` | 1.7 |
| Label / price / eyebrow | Jost | 11–13px | 500 | `0.14em` uppercase | 1.4 |
| Arabic display | Reem Kufi | 56–76px | 400 | `0` | 1.35 |
| Arabic body | Tajawal | 17–19px | 300 | `0` | 1.9 |

**Arabic type sets larger and looser than Latin at the same optical size.** Arabic body runs
~1px larger and needs roughly `+0.2` line-height. A page that simply mirrors the Latin scale will
look cramped to Nadia — who is the repeat customer.

**Avoid:** any slab serif · any humanist sans (Open Sans, Lato, Source Sans — they read
institutional) · Inter or Roboto anywhere · condensed anything · script or handwritten faces ·
Playfair Display · and **never** mix scripts inside a sentence.

---

## 05 — Imagery — art direction under D2

**This section exists because of `decisions.md` D2: the brand launches with AI-generated product
imagery, with the risk stated and accepted.** The direction below is written to make that
constraint work honestly, not to hide it.

**Overall aesthetic:** low-key still life. One light source, raking from the upper left, falling
off fast into wine shadow. Velvet or matte stone surfaces. Closer to a jewellery catalogue than a
food blog. Never bright, never overhead-flat-lay, never white-background e-commerce.

**Subject matter, in priority order**
1. The box — closed, held, or being handed over. **The handover is the brand's territory, and it
   is also the shot AI renders most convincingly**, because it is about gesture and light rather
   than food texture.
2. Material and texture — velvet, stone, the gold of the mark, a hairline of chocolate.
3. Product, at catalogue scale.
4. **Never** an extreme appetite close-up presented as the specific product being sold — per D2
   rule 1. That is the shot that generates complaints, and it is also the one AI gets wrong.

**Colour treatment:** warm-shifted, deep shadows, restrained highlights. A `mix-blend-multiply`
wine layer at 15–25% over every image so the whole library reads as one world. A
`bg-gradient-to-t from-[#170509]/70` overlay on anything carrying text. **The treatment layer is
doing double duty here** — it unifies the library *and* it pulls images away from photoreal
literalism toward brand world, which is exactly what D2 rule 4 requires.

**Non-negotiable under D2**
- Product images render at **catalogue scale** — max ~480px wide in a card. Never full-bleed hero.
- Every card states the real spec in text beside the image. **Text carries the promise; the image
  carries the mood.** This is the single rule that keeps the brand honest.
- Fixed aspect ratios — `4:5` product, `16:9` lifestyle, `1:1` collection tiles — so a real shoot
  drops in later with zero rework. Build the slots now.
- Never caption a render "pictured" or "as shown".

**Avoid:** white seamless backgrounds · overhead flat-lays with scattered props · hands in frame
holding a piece toward camera · steam, splashes, mid-air chocolate drizzle · confetti bokeh ·
anything from the current carousels' floating-ingredients treatment, which reads as a supermarket
promotion rather than a luxury house.

---

## 06 — Iconography

Hairline line icons. Stroke `1.25px`, `stroke-linecap: round`, drawn on a 24px grid, gold or
cream, never filled and never in a circle. Utilitarian and nearly invisible — the identity does
its talking through type and space, and a decorative icon set would compete with the mark.

**The vesica is the only branded shape.** It may be reused as a bullet, a divider, a section
marker, or a repeating packaging pattern at 6–8% opacity. That reuse is what builds recognition —
one shape, everywhere, never redrawn.

Permitted set, and no more: WhatsApp, Instagram, location, clock/lead-time, box, arrow.

---

## 07 — Design Principles

**Darkness is the ground.**
The brand lives on wine and ink. Light backgrounds are the exception, used once, for long reading.
Every design decision starts from a dark canvas — which means contrast, glow, and gold placement
are the primary tools, not colour variety.

**Space is the luxury.**
The most expensive element on any page is the part with nothing in it. Generous margins, large
type, and few elements per screen. **If a layout feels too empty, it is probably correct** — the
instinct to fill space is the instinct that makes a brand look cheap.

**Gold is punctuation.**
Gold marks the beginning of a thought, never fills a shape. It appears on the mark, on headings,
on hairline rules, and on one call to action per screen. The moment gold becomes a background, the
brand has become a wedding invitation.

**Everything is inscribed.**
Letterforms look carved: wide tracking, sharp terminals, no rounded softness, no drop shadows on
type. Both scripts share this — Trajan and Kufic were both cut into stone, and that shared origin
is the concept holding the bilingual system together.

---

## 08 — Brand Expressions

**Instagram**
- **Avatar: replace with the Mark B vesica on `ink`.** Mark only, not the lockup — the lockup is
  illegible at avatar size, which is exactly why Mark A was there. **This is the first fix, and it
  is the one that makes the site and the feed look like the same company.**
- Grid alternates: product on wine → typographic quote on ink → material texture. Never three
  product posts consecutively.
- Captions per `voice.md` — one thought per line, four lines maximum.

**Website**
Dark, wine-grounded, generous vertical rhythm. Cinzel wordmark in the header, Cormorant display,
Jost body. One gold CTA per screen. Full RTL Arabic — mirrored layout, not a mirrored English
page. Every interactive element gets hover, `focus-visible`, and active states. Animate `transform`
and `opacity` only, with spring easing; never `transition-all`. Grain layer over all full-bleed
dark sections.

**Packaging**
Matte wine board, gold foil **debossed** — the vesica pressed into the lid, catching light rather
than printed on. Interior in `ink`. Bilingual lockup. The gift card carries the tagline and
nothing else. **Packaging is where D2's weakness stops mattering** — a customer holding a
well-made box does not care what the website render looked like. It is the highest-leverage spend
in the brand after the mark itself.

**Stationery and corporate**
Wine card stock, gold foil mark, Jost 300 for details. The corporate one-pager is the one place
`paper` ground is allowed, so it survives being photocopied by Hazem's procurement team.

**Delivery and unboxing**
Wine tissue, a gold vesica sticker as the seal. The seal is the whole idea — the customer breaks
the mark to open the box, and that is the moment the brand is remembered.

---

## 09 — Open Items

1. **Mark B needs redrawing as clean vector.** What exists is a raster from a video cover. Before
   packaging is printed, it needs proper outlines: SVG, plus `.ai`/`.eps`, plus a mono version and
   a one-colour foil version.
2. **The Arabic wordmark «تمور نادرة» does not exist yet** and must be drawn — Reem Kufi is the
   starting point, not the final letterforms. Custom kerning at minimum.
3. **The Instagram avatar is the fastest visible win in the entire project.** One asset, replaces
   the retired mark, and it costs an hour.
