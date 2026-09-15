# HVAC AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names an HVAC contractor when
someone asks it a buying question, paired with a homepage technology and content crawl across
the same industry.

**This industry has no live public report page yet.** Unlike the other five industries in this
release, kkvlabs.com does not yet publish a `/research/...` index page for HVAC, so there is no
canonical URL to link and no live `data.csv` route to diff `cities.csv` against. This dataset
was exported straight from the source JSON the same way the other five were.

## How this was collected

Google AI Mode answers were captured across 60 cities [hvac-cities.json;
HVAC-INDEX-FINDINGS-2026-09-12.md]. The homepage technology and content crawl ran 2026-09-12
[hvac-stack.json]: 577 homepages attempted, 506 read, 40 blocked by bot walls. "Named" is the
148 read sites whose company Google AI Mode named in its city answer; "unnamed" is the other
358 [hvac-stack.json].

All comparisons in this dataset are same-day, not causes [HVAC-INDEX-FINDINGS-2026-09-12.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, computed from `hvac-cities.json`
  using the same column layout and filter the other five industries' live data.csv routes use
  [hvac-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `hvac-stack.json` [hvac-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [hvac-stack.json].

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
| tier | GREEN (3+ named), YELLOW (2), RED (1) |
| tierNote | Manual note on why a tier was set by hand, blank if none |
| aiCheckedOn | ISO date the AI answer was captured |

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, vendors, crm, chat, leadCapture, pixels, certifications, brands, financing, reviewWidgets, social, services, weightBuckets, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- Every one of the 60 cities checked came back GREEN, no YELLOW, no RED, 299 companies named
  in all, a median of 5 per city, so there is no empty city in this market to point a discovery
  pitch at [HVAC-INDEX-FINDINGS-2026-09-12.md].
- Certifications, brand dealer tiers and "free estimate" offers all show flat or backwards
  relationships to being named; treat them as non-signals, not visibility levers
  [HVAC-INDEX-FINDINGS-2026-09-12.md].
- Homepage only, detection by known scripts and links; every technology share is a floor
  [HVAC-INDEX-FINDINGS-2026-09-12.md].
- **sitesFailed reconciliation.** `hvac-stack.json`'s `sitesFailed` is 31, while
  HVAC-INDEX-FINDINGS-2026-09-12.md's prose calls out "24 other failures" separately. These
  reconcile: the JSON bundles the doc's 24 other failures (dead TLS handshakes, timeouts, dead
  DNS) together with the 7 sites that answered but gave back nothing readable (24 + 7 = 31).
- No canonical live report page exists yet for this industry; treat this dataset as pre-release
  until kkvlabs.com publishes `/research/hvac-ai-visibility-index-2026` (or similar).

## Canonical page

Not yet published on kkvlabs.com.
