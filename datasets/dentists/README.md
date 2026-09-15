# Dental AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a dental practice when
someone asks it a buying question, paired with a homepage technology and content crawl across
the same industry. It is the dataset behind the live report at
https://www.kkvlabs.com/research/dental-ai-visibility-index-2026.

## How this was collected

Google AI Mode answers were captured 2026-09-08 across 40 cities [dentists-cities.json;
DENTAL-INDEX-FINDINGS-2026-09-11.md]. The homepage technology and content crawl ran 2026-09-11
[dentists-stack.json]: 435 homepages attempted, 366 read, 38 blocked by bot walls. "Named" is
the 84 read sites whose practice Google AI Mode named in its city answer; "unnamed" is the
other 282 [dentists-stack.json].

All comparisons in this dataset are same-day, not causes [DENTAL-INDEX-FINDINGS-2026-09-11.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, reproduced column for column from
  the live `/research/dental-ai-visibility-index-2026/data.csv` route, computed from
  `dentists-cities.json` [dentists-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `dentists-stack.json` [dentists-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [dentists-stack.json].

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
[dental-ai-visibility-index-2026/data.csv route.ts].

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, crm, leadCapture, pixels, certifications, financing, reviewWidgets, social, services, weightBuckets, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- Homepage only, detection by known scripts and links; new or self-hosted tools read as "none",
  and every technology share is a floor [DENTAL-INDEX-FINDINGS-2026-09-11.md].
- CareCredit shows on 94 sites (a quarter of the index) at an identical 26 percent share among
  named and unnamed practices, which is why it is documented here as a non-signal rather than a
  visibility lever [DENTAL-INDEX-FINDINGS-2026-09-11.md].
- 29 of 40 cities came back GREEN and 3 RED in this run; small-city tiers can rest on a handful
  of names, so read the exact counts in `cities.csv` before quoting a percentage
  [DENTAL-INDEX-FINDINGS-2026-09-11.md].

## Canonical page

https://www.kkvlabs.com/research/dental-ai-visibility-index-2026
