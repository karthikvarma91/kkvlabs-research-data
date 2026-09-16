# KKV Labs AI Local Visibility Index Datasets

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22765584.svg)](https://doi.org/10.5281/zenodo.22765584)

September 2026 edition. Seven industries, one question each: when someone asks Google AI Mode a
buying question in a given city, does it name a local business, and which one. Paired with a
homepage technology and content crawl of the same industry, so a claim of visibility can be
checked against what the business actually publishes. Each industry's dataset lives in
`datasets/<industry>/` with a `cities.csv`, a `stack.csv`, a `meta.json` and its own `README.md`.
The live reports are at https://www.kkvlabs.com/research. A separate, cross-industry dataset,
`datasets/citation-sources/`, maps which domains an AI answer actually cites alongside the
businesses it names; see its own README.

All comparisons in every dataset here are same-day, not causes: a business named by the AI on
the day of the check was named for many reasons the crawl cannot see. Read the per-industry
README before quoting a figure.

## The industries

**Med spas.** 245 cities screened, 1,352 of 1,531 homepages read, 341 named versus 1,011
unnamed [STACK-FINDINGS-2026-09-10.md]. In `cities.csv`, `sitesScreened` and `clinicsNamed` are
different populations (our screening list versus who the AI named) and are not meant to
reconcile city by city; see `datasets/medspa/README.md` before comparing them. Clinics on
Zenoti or Boulevard booking software are
about twice as common among AI-named med spas as among the rest (Zenoti 10 vs 6 percent,
Boulevard 10 vs 5) [STACK-FINDINGS-2026-09-10.md]. Only 40 percent of med spas show a price
anywhere on the site, and it makes no difference to being named [STACK-FINDINGS-2026-09-10.md].
Named clinics list more treatments (median 9 vs 7) and write longer homepages (987 vs 868 words)
[STACK-FINDINGS-2026-09-10.md].

**Roofers.** 60 cities, 569 homepages attempted, 520 read, 147 named versus 373 unnamed
[ROOFING-INDEX-FINDINGS-2026-09-11.md]. Claiming a manufacturer certification does nothing for
AI visibility: 26 percent of AI-named roofers claim one and 25 percent of the rest do
[ROOFING-INDEX-FINDINGS-2026-09-11.md]. Only 15 percent publish a price and 14 percent a licence
number [ROOFING-INDEX-FINDINGS-2026-09-11.md]. An llms.txt file is a website-builder artifact,
not a strategy: every Duda site and every Wix site has one, against 34 percent of WordPress
sites [ROOFING-INDEX-FINDINGS-2026-09-11.md].

**Dentists.** 40 cities, 435 homepages attempted, 366 read, 84 named versus 282 unnamed
[dentists-stack.json; DENTAL-INDEX-FINDINGS-2026-09-11.md]. Provider credentials run backwards:
DDS or DMD appears on 37 percent of AI-named sites and 48 percent of the rest
[DENTAL-INDEX-FINDINGS-2026-09-11.md]. What separates named practices is the range of work they
list, not credentials: Invisalign 76 vs 51 percent, emergency dentistry 70 vs 52
[DENTAL-INDEX-FINDINGS-2026-09-11.md]. CareCredit shows on a quarter of all sites at an
identical 26 percent share among named and unnamed, a non-signal
[DENTAL-INDEX-FINDINGS-2026-09-11.md].

**Personal injury law firms.** 60 cities, 875 homepages attempted, 685 read, 187 named versus
498 unnamed [law-firms-stack.json; LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md]. Every one of the 60
cities came back GREEN, 297 firms named in all, a median of 5 per city: there is no empty city
in this market, the pitch is displacement, not discovery
[LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md]. Directory listings (Avvo, Justia, FindLaw) show no
relationship, or a backwards one, to being named [LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md]. Named
firms list more practice areas (median 12 vs 9) and put a recovered dollar amount on the
homepage more often (48 vs 33 percent) [LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md].

**Chiropractors.** 40 cities, 602 homepages attempted, 460 read, 105 named versus 355 unnamed
[chiropractors-stack.json; CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md]. 39 of 40 cities came back
GREEN, 192 practices named in all [CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md]. Credentials do
not separate named from unnamed practices, and schema adoption runs backwards: named practices
are worse on structured-data lines than unnamed ones
[CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md]. Named practices write more (1,135 vs 821 words) and
list more services (12 vs 10) [CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].

**HVAC contractors.** 60 cities, 577 homepages attempted, 506 read, 148 named versus 358 unnamed
[hvac-stack.json; HVAC-INDEX-FINDINGS-2026-09-12.md]. Every city came back GREEN, 299 companies
named in all [HVAC-INDEX-FINDINGS-2026-09-12.md]. Years in business, licensing, NATE
certification and manufacturer dealer tiers are all flat between named and unnamed companies
[HVAC-INDEX-FINDINGS-2026-09-12.md]. What separates named companies is what they publish:
financing pages (68 vs 47 percent), blogs (72 vs 51), maintenance plan pages (42 vs 27)
[HVAC-INDEX-FINDINGS-2026-09-12.md]. Live report: https://www.kkvlabs.com/research/hvac-ai-visibility-index-2026 (published 15 Sep 2026);
`cities.csv` matches its data.csv route.

**Plumbers.** 60 cities, 443 homepages attempted, 409 read, 126 named versus 283 unnamed
[plumbers-stack.json; PLUMBING-INDEX-FINDINGS-2026-09-15.md]. Only 144 of the 305 companies
Google AI Mode named across the 60 cities resolved to a real website at all, 47 percent, the
lowest resolution rate of the seven trades in this project: a plumbing company's name is built
almost entirely from category and shared-trade words, leaving a guessed hostname little to
verify against [PLUMBING-INDEX-FINDINGS-2026-09-15.md]. Named plumbers run field service and
dispatch software at more than double the rate of unnamed ones, 31 vs 13 percent, and carry an
online booking route 56 vs 33 [PLUMBING-INDEX-FINDINGS-2026-09-15.md]. A licence or registration
number sits on only 19 percent of homepages, though every one of these companies is required to
hold one [PLUMBING-INDEX-FINDINGS-2026-09-15.md]. See `datasets/plumbers/README.md`.

## Citation sources

`datasets/citation-sources/` is a different shape of dataset: not a per-industry city crawl, but
123 Google AI Mode answers (20 to 21 cities in each of the same six industries above, excluding
plumbers) read for which domains they actually cited alongside the named businesses. The
business's own site and its Google Business Profile are cited in 70 percent or more of answers
in every industry; past those two, the directory that shows up changes by trade (Justia and
Super Lawyers for law firms, Zocdoc and Healthgrades for dentists and chiropractors, Angi and
Thumbtack for roofers) [CITATION-SOURCES-FINDINGS-2026-09-15.md]. See
`datasets/citation-sources/README.md`.

## How to cite

KKV Labs (2026). AI Local Visibility Index datasets, September 2026 edition. Karthik Varma, KKV
Labs LLC. https://www.kkvlabs.com/research. DOI 10.5281/zenodo.22765584 (this version) and
10.5281/zenodo.22765583 (all versions). Licence CC BY 4.0.

See also `CITATION.cff` and `.zenodo.json`.

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0). Full text in `LICENSE`.

## Reproducing this export

`scripts/export.py` reads the source JSON files in kkvlabs-landing's `src/app/data/` and writes
every `datasets/<industry>/{cities.csv,stack.csv,meta.json}` in this repository. Run it from the
repository root with `python3 scripts/export.py` (Python 3, standard library only).

## Changelog

- 2026-09-16: plumbers dataset added (seventh industry); citation-sources dataset added
  (cross-industry, not a per-industry city crawl).
- 2026-09-15: first release, 6 industries.
