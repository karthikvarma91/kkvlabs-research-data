# Chiropractic AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a chiropractic practice when
someone asks it a buying question, paired with a homepage technology and content crawl across
the same industry. It is the dataset behind the live report at
https://www.kkvlabs.com/research/chiropractic-ai-visibility-index-2026.

## How this was collected

Google AI Mode answers were captured 2026-09-08, across 40 cities
[chiropractors-cities.json; CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md]. The homepage technology
and content crawl ran 2026-09-12 [chiropractors-stack.json]: 602 homepages attempted, 460 read,
92 blocked by bot walls. "Named" is the 105 read sites whose practice Google AI Mode named in
its city answer; "unnamed" is the other 355 [chiropractors-stack.json].

All comparisons in this dataset are same-day, not causes
[CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, reproduced column for column from
  the live `/research/chiropractic-ai-visibility-index-2026/data.csv` route, computed from
  `chiropractors-cities.json` [chiropractors-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `chiropractors-stack.json` [chiropractors-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [chiropractors-stack.json].

### cities.csv column dictionary

| Column | Meaning |
| --- | --- |
| cityState | "City, ST" |
| state | Two-letter state code |
| sitesScreened | Homepages found and read for that city |
| noSchema | Screened sites with no structured data detected |
| noViewport | Screened sites with no mobile viewport meta tag |
| staleCopyright | Screened sites with a stale footer copyright year |
| practicesNamed | Number of practices Google AI Mode named in that city's answer |
| namedPractices | The practices named, semicolon-separated |
| tier | GREEN (3+ named), YELLOW (2), RED (1) |
| tierNote | Manual note on why a tier was set by hand, blank if none |
| aiCheckedOn | ISO date the AI answer was captured |

Only cities with a captured AI answer are included, matching the live data.csv route
[chiropractic-ai-visibility-index-2026/data.csv route.ts].

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, vendors, crm, chat, leadCapture, pixels, certifications, techniques, financing, reviewWidgets, social, services, weightBuckets, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- The Oxygen page builder false positive that affected the med spa index (a signature matching
  GoDaddy's `CONTACT_SECTION_TITLE_REND` heading id) reached this crawl too, publishing Oxygen
  on 10 sites, 9 of them GoDaddy. Here it was fully recomputed from `tools/html-cache-chiropractors`
  and corrected: the true count is 0, and the row is removed from `stack.csv`
  [STACK-FINDINGS-2026-09-10.md; CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].
- Schema runs backwards in this market: named practices are worse on structured-data adoption
  than unnamed ones on every line measured. This is documented as open ground, not a gap to
  catch up on [CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].
- Homepage only, detection by known scripts and links; every technology share is a floor
  [CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].
- 39 of 40 cities came back GREEN and 1 YELLOW in this run; small-city tiers can rest on a
  handful of names, so read the exact counts in `cities.csv` before quoting a percentage
  [CHIROPRACTIC-INDEX-FINDINGS-2026-09-12.md].

## Canonical page

https://www.kkvlabs.com/research/chiropractic-ai-visibility-index-2026
