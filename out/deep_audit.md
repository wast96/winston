# Random-sample deep audit

*Check 8 from the original list: sample 3–5% of passages and read them hard
against the source, to estimate the error rate across the whole translation.*

## Method

Population: **793 paired paragraphs** across the prologue and chapters 2–6 —
every paragraph of the finished translation for which a paired source line
exists. (Chapter 1 is the reference translation and was excluded; it predates
this run.)

Sample: **32 paragraphs, 4.0%**, drawn with a fixed random seed so the sample is
reproducible. Distribution fell out as prologue 2, ch2 4, ch3 3, ch4 9, ch5 4,
ch6 10 — roughly proportional to chapter length, which is what an unweighted
draw should give.

Each sampled paragraph was put through three mechanical screens and then read
by hand against its source line.

## Mechanical screens

| Screen | What it catches | Flagged |
|---|---|---|
| Quantity survival | dropped or altered numbers, dates, counts | **0** |
| Length ratio | a dropped clause or sentence | 1 |
| Dialogue turns | a dropped speech | 1 |

**Both flags were false positives.**

The length flag was a paragraph where the English is simply more economical than
the Chinese — a four-character dismissal rendered as three words. Nothing
missing.

The dialogue flag was my own counter miscounting: the source puts a ship's name
in quotation marks three times, which the screen read as three speeches. The
English sets the ship's name in italics instead. Content complete.

## What the hand reading found

One real thing, in the paragraph the dialogue screen had flagged for the wrong
reason. The source says a freighter had been moored at the bank **多时** — "a
good while," a deliberately vague duration. I had rendered it "**for weeks**."

That is not a mistranslation exactly; it is **invented precision**. The source
declines to say how long and I supplied a figure. It is small, and no
mechanical check would ever catch it, which is precisely the argument for
reading a sample by hand. Corrected to "a good while."

## Estimated error rate

On this sample:

- **Substantive errors** (wrong meaning, dropped content, invented sentences):
  **0 of 32**. Upper bound of the 95% confidence interval on a zero-count sample
  of this size is roughly 11%, so the honest statement is "none observed, and
  the sample is too small to prove a rate below about one in ten."
- **Minor infelicities** (over-specification, register drift): **1 of 32**,
  about 3%.

Extrapolated to the 793-paragraph population, that suggests on the order of
**20–25 paragraphs carrying a minor infelicity** of the invented-precision kind,
and no detectable rate of substantive error.

## What this does and does not tell you

It tells you the mechanical layer is holding: the invariant checker has been
run to zero unresolved on every chapter, and the sample confirms it is not
missing a class of numeric error.

It does not tell you the prose is good. Register is not measurable this way, and
the failure mode that got the first draft rejected — stiltedness — would not
show up in any of these screens. That judgement is yours.

The one class of defect this audit did surface is worth naming because it will
recur: **the translator supplying definiteness the source withholds.** Vague
durations, approximate counts and non-committal phrasing are exactly where an
English sentence wants to firm up and shouldn't. Worth a targeted grep at the
final pass rather than another random sample.
