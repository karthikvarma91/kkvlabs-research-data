# Roofing AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a roofing company when
someone asks it a buying question, paired with a homepage technology and content crawl across
the same industry. It is the dataset behind the live report at
https://www.kkvlabs.com/research/roofing-ai-visibility-index-2026.

## How this was collected

Google AI Mode answers were captured 2026-09-10 across 60 cities [roofers-cities.json;
ROOFING-INDEX-FINDINGS-2026-09-11.md]. The homepage technology and content crawl ran
2026-09-11 from India with `tools/crawl_stack.py --industry roofers`: 569 homepages attempted,
520 read, 33 blocked by bot walls (Cloudflare interstitial, SiteGround captcha, nginx 403), 16
other failures (timeout, dead TLS, 5xx) [ROOFING-INDEX-FINDINGS-2026-09-11.md]. "Named" is the
147 read sites whose company Google AI Mode named in its city answer; "unnamed" is the other
373 [ROOFING-INDEX-FINDINGS-2026-09-11.md]. Every technology share is a floor: a tool can be in
use without leaving a trace on the homepage [ROOFING-INDEX-FINDINGS-2026-09-11.md].

All comparisons in this dataset are same-day, not causes [ROOFING-INDEX-FINDINGS-2026-09-11.md].

The count of sites "found" in a city can never be fewer than the count "screened" there; the
build pipeline enforces this by taking the max of the two [project_kkvlabs_landing memory note;
kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city with a captured AI answer, reproduced column for column from
  the live `/research/roofing-ai-visibility-index-2026/data.csv` route, computed from
  `roofers-cities.json` [roofers-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `roofers-stack.json` [roofers-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [roofers-stack.json].

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

Only cities with a captured AI answer are included, matching the live data.csv route
[roofing-ai-visibility-index-2026/data.csv route.ts].

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

- The named set (`tools/named-roofers-domains.csv`) holds 277 rows, one per company named
  across 60 cities; 115 of those carry no resolvable domain and are excluded from the
  named-versus-unnamed technology comparison, which therefore rests on 147 of the 277 companies
  the AI named, about 53 percent of them [ROOFING-INDEX-FINDINGS-2026-09-11.md].
- Homepage only. Every technology share is a floor
  [ROOFING-INDEX-FINDINGS-2026-09-11.md].
- Detection is by known scripts and links; new or self-hosted tools read as "none"
  [ROOFING-INDEX-FINDINGS-2026-09-11.md].
- Some named-versus-unnamed comparisons rest on fewer than 20 named sites; quote the counts,
  never a "times as likely" framing [ROOFING-INDEX-FINDINGS-2026-09-11.md].

## Canonical page

https://www.kkvlabs.com/research/roofing-ai-visibility-index-2026
