# Med Spa AI Visibility Index, September 2026 edition

What this is: a city-by-city read of whether Google AI Mode names a med spa when someone asks
it a buying question, paired with a homepage technology and content crawl across the same
industry. It is the dataset behind the live report at
https://www.kkvlabs.com/research/med-spa-ai-visibility-index-2026.

## How this was collected

Screening and Google AI Mode answers were captured 2026-09-08 across 245 cities
[medspa-cities.json]. The homepage technology and content crawl ran 2026-09-10 from India with
`tools/crawl_stack.py`: 1,531 homepages attempted, 1,352 read, 179 blocked by bot walls
(SiteGround captcha, Cloudflare, nginx 403) [STACK-FINDINGS-2026-09-10.md]. "Named" is the 341
read sites whose clinic Google AI Mode named in its city answer; "unnamed" is the other 1,011
[STACK-FINDINGS-2026-09-10.md]. Every technology share is a floor: a tool can be in use without
a trace on the homepage [STACK-FINDINGS-2026-09-10.md].

All comparisons in this dataset are same-day, not causes: named clinics were named for many
reasons the crawl cannot see [STACK-FINDINGS-2026-09-10.md].

The count of sites "found" in a city can never be fewer than the count "screened" there;
the build pipeline enforces this by taking the max of the two
[project_kkvlabs_landing memory note; kkvlabs-outreach/tools/build_city_data.py].

## Files

- `cities.csv`: one row per city, reproduced column for column from the live
  `/research/med-spa-ai-visibility-index-2026/data.csv` route, computed from
  `medspa-cities.json` [medspa-cities.json].
- `stack.csv`: one row per (section, name) technology or content signal, computed from
  `medspa-stack.json` [medspa-stack.json].
- `meta.json`: crawl accounting figures for the homepage crawl [medspa-stack.json].

### cities.csv column dictionary

| Column | Meaning |
| --- | --- |
| cityState | "City, ST" |
| state | Two-letter state code |
| sitesScreened | Homepages found and read for that city |
| noSchema | Screened sites with no structured data detected |
| noViewport | Screened sites with no mobile viewport meta tag |
| staleCopyright | Screened sites with a stale footer copyright year |
| clinicsNamed | Number of clinics Google AI Mode named in that city's answer |
| tier | GREEN (3+ named), YELLOW (2), RED (1) |
| aiCheckedOn | ISO date the AI answer was captured |

No clinic names or domains are in this file: the count named is the finding, not a directory
of who was named [medspa-cities.json/data.csv route].

### stack.csv column dictionary

| Column | Meaning |
| --- | --- |
| section | Technology or content category (platform, builders, booking, pixels, messaging, emailTools, finance, treatments, credentials, social, signals) |
| name | The specific technology, vendor or content feature |
| sites | Count of read homepages carrying it |
| share | Percent of all read homepages carrying it |
| namedShare | Percent among AI-named homepages |
| unnamedShare | Percent among not-named homepages |

## Known limitations

- **Oxygen builder count is a known false positive, pending a re-crawl.** The published figure
  in `stack.csv` (builders section, "Oxygen") is 28 sites, corrected down from a first published
  31 after a signature bug (matching GoDaddy's own `CONTACT_SECTION_TITLE_REND` heading id as if
  it were the Oxygen builder) was found and fixed. 27 of the original 31 flagged sites cannot be
  re-read offline because HTML caching only started after the 2026-09-10 run, and 25 of those 27
  are recorded as GoDaddy Website Builder, so they are almost certainly the same false positive.
  The true count is expected to be about 3, which would put Oxygen below the 10-site floor the
  builders table uses and drop it from the table altogether. Do not quote an Oxygen figure until
  the 27 are re-crawled [STACK-FINDINGS-2026-09-10.md]. The value in `stack.csv` is the current
  published figure (28), not the corrected estimate.
- Homepage only. A booking tool behind a "Book now" page, a price on a menu page, or a
  credential on the About page is not counted. Every technology share is a floor
  [STACK-FINDINGS-2026-09-10.md].
- Detection is by known scripts and links; new or self-hosted tools read as "none"
  [STACK-FINDINGS-2026-09-10.md].
- 179 sites (12 percent) blocked the crawler; their absence could tilt the platform mix, since
  bot walls are common on SiteGround and Cloudflare hosts [STACK-FINDINGS-2026-09-10.md].
- The named set is the named clinics that were also in the screened set (341 of 1,352), so it
  under-represents big chains and over-represents small markets [STACK-FINDINGS-2026-09-10.md].
- A handful of signatures were found unreliable and fixed before publishing, including a
  "Boulevard" match on street addresses (261 affected sites refetched, 207 became 86) and "Tebra"
  matching "vertebra" [STACK-FINDINGS-2026-09-10.md].

## Canonical page

https://www.kkvlabs.com/research/med-spa-ai-visibility-index-2026
