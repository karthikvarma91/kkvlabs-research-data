# Plumbing AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a plumbing company when
someone asks it a buying question, paired with a homepage technology and content crawl across
the same industry, and a name-to-website resolution audit that is the headline finding of this
release.

## How this was collected

Google AI Mode was asked "best plumber in <City> <State>" across 60 cities, captured
2026-09-15, and named 305 companies in all [plumbers-cities.json;
PLUMBING-INDEX-FINDINGS-2026-09-15.md]. One individual freelancer (not a company) was excluded
from that count. The homepage technology and content crawl ran 2026-09-16: 443 homepages
attempted, 409 read and counted, 11 blocked by bot walls, 23 other failures
[plumbers-stack.json].

**The headline finding of this release.** Only 144 of the 305 named companies (47 percent, the
lowest resolution rate of the six trades in this project so far) could be matched to a real,
live website at all: 105 matched a domain already in the screened candidate list, 39 more were
found by a verified hostname guess. The other 161 have no domain on record. A plumbing
company's name is built almost entirely from category and shared-trade words ("plumbing",
"plumber", "drain", "rooter", "water", "service", plus "heating"/"cooling"/"mechanical"
borrowed from HVAC), so a guessed hostname usually has nothing distinctive left to verify
against [PLUMBING-INDEX-FINDINGS-2026-09-15.md].

Of the 144 resolved domains (143 unique, one business named twice under two names in the same
city), all were crawled: 126 were read and counted as "named" in the technology crawl, 7 sat
behind a bot wall, 9 failed for another reason, and 1 was an unreadable stub. A follow-up audit
tested every resolved row for a name match, a city match and enough plumbing content: 23 of the
144 failed the letter of that test, 8 turned out to be real wrong-domain matches and were
blanked, and 15 were kept with the evidence written down because the failure was in the audit's
own name-matching (an apostrophe, an ampersand, a franchise page that never repeats the named
city) rather than a wrong site [PLUMBING-INDEX-FINDINGS-2026-09-15.md]. "Named" in `cities.csv`
and `stack.csv` is these 126 sites; "unnamed" is the other 283.

All comparisons in this dataset are same-day, not causes [PLUMBING-INDEX-FINDINGS-2026-09-15.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, computed from `plumbers-cities.json`
  using the same column layout and filter the other industries' live data.csv routes use
  [plumbers-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `plumbers-stack.json` [plumbers-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [plumbers-stack.json].

### cities.csv column dictionary

| Column | Meaning |
| --- | --- |
| cityState | "City, ST" |
| state | Two-letter state code |
| sitesScreened | Homepages found and read for that city |
| noSchema | Screened sites with no structured data detected |
| noViewport | Screened sites with no mobile viewport meta tag |
| staleCopyright | Screened sites with a stale footer copyright year |
| companiesNamed | Number of companies Google AI Mode named in that city's answer |
| namedCompanies | The companies named, semicolon-separated |
| tier | GREEN (3+ named), YELLOW (2), RED (1). Every one of the 60 cities in this run is GREEN |
| tierNote | Manual note on why a tier was set by hand, blank if none |
| aiCheckedOn | ISO date the AI answer was captured |

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, vendors, crm, chat, leadCapture, pixels, certifications, brands, financing, reviewWidgets, social, services, weightBuckets, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages (the 126 verified sites) |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- The named-domain resolution rate (144 of 305, 47 percent) is the lowest of the six trades in
  this project so far, and it is a structural fact about how plumbing companies are named, not
  a data quality gap: any percentage built from the named-versus-unnamed comparison in this
  dataset rests on the 126 of 305 AI-named companies (41 percent) that could be verified end to
  end [PLUMBING-INDEX-FINDINGS-2026-09-15.md].
- Brand and dealer-tier claims are structurally thinner in plumbing than in HVAC (11 percent any
  brand vs HVAC's 44, 0 percent any dealer tier vs HVAC's 12), because plumbing fixture and
  water-heater manufacturers do not run factory-authorized-dealer programs the way HVAC
  equipment makers do. This is a market difference, not a data quality issue
  [PLUMBING-INDEX-FINDINGS-2026-09-15.md].
- City tier discrimination is limited this round: every one of the 60 cities is GREEN, so the
  tier column is not useful for ranking cities against each other; use the raw readiness inputs
  (schema, booking route, insurance and licence language, review count) instead
  [PLUMBING-INDEX-FINDINGS-2026-09-15.md].
- Homepage only, detection by known scripts and links; every technology share is a floor
  [PLUMBING-INDEX-FINDINGS-2026-09-15.md].
- 16 of the 305 named companies' resolved domains could not be re-fetched live at audit time (a
  TLS handshake failure, a live-network artefact rather than a dead domain); those rows keep the
  domain the resolver found, unverified by the audit's own live re-check
  [PLUMBING-INDEX-FINDINGS-2026-09-15.md].

## Canonical page

https://kkvlabs.com/research/plumbing-ai-visibility-index-2026
