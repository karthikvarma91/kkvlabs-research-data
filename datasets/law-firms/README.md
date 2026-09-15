# Law Firm AI Visibility Index, personal injury, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a personal injury law firm
when someone asks it a buying question, paired with a homepage technology and content crawl
across the same industry. It is the dataset behind the live report at
https://www.kkvlabs.com/research/law-firm-ai-visibility-index-2026.

## How this was collected

Google AI Mode answers were captured 2026-09-09 (27 cities) and 2026-09-11 (33 cities), 60
cities in all [law-firms-cities.json; LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md]. The homepage
technology and content crawl ran 2026-09-11 [law-firms-stack.json]: 875 homepages attempted,
685 read, 130 blocked by bot walls. "Named" is the 187 read sites whose firm Google AI Mode
named in its city answer; "unnamed" is the other 498 [law-firms-stack.json].

All comparisons in this dataset are same-day, not causes
[LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, reproduced column for column from
  the live `/research/law-firm-ai-visibility-index-2026/data.csv` route, computed from
  `law-firms-cities.json` [law-firms-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `law-firms-stack.json` [law-firms-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [law-firms-stack.json].

### cities.csv column dictionary

| Column | Meaning |
| --- | --- |
| cityState | "City, ST" |
| state | Two-letter state code |
| sitesScreened | Homepages found and read for that city |
| noSchema | Screened sites with no structured data detected |
| noViewport | Screened sites with no mobile viewport meta tag |
| staleCopyright | Screened sites with a stale footer copyright year |
| firmsNamed | Number of firms Google AI Mode named in that city's answer |
| namedFirms | The firms named, semicolon-separated |
| tier | GREEN (3+ named), YELLOW (2), RED (1) |
| tierNote | Manual note on why a tier was set by hand, blank if none |
| aiCheckedOn | ISO date the AI answer was captured |

Only cities with a captured AI answer are included, matching the live data.csv route
[law-firm-ai-visibility-index-2026/data.csv route.ts].

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, vendors, crm, leadCapture, pixels, certifications, financing, reviewWidgets, social, services, weightBuckets, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- Every one of the 60 cities checked came back GREEN, no YELLOW, no RED, 297 firms named in all,
  a median of 5 per city, so there is no empty city in this market to point a discovery pitch at
  [LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md].
- Directory listings (Avvo, Justia, Lead Counsel, FindLaw) show no relationship, or a backwards
  one, to being named; treat them as non-signals, not visibility levers
  [LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md].
- Homepage only, detection by known scripts and links; every technology share is a floor
  [LAW-FIRMS-INDEX-FINDINGS-2026-09-11.md].

## Canonical page

https://www.kkvlabs.com/research/law-firm-ai-visibility-index-2026
