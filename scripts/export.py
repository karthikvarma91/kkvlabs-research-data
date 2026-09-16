#!/usr/bin/env python3
"""Export cities.csv, stack.csv and meta.json for each industry dataset.

Reads only from kkvlabs-landing/src/app/data/<slug>-cities.json and
<slug>-stack.json. Writes datasets/<industry>/{cities.csv,stack.csv,meta.json}.

cities.csv reproduces, column for column, the same rows the live
/research/<index>/data.csv route serves (computed the same way the route's
source does: same column list, same filter, same sort), so it can be diffed
directly against the live file. Five of the six industries here have a live
index page; hvac does not yet.

Run from anywhere:
    python3 scripts/export.py
"""
import csv
import io
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LANDING_DATA = Path(
    "/Users/karthikvarma/Code/kkvlabs-landing/src/app/data"
)

# industry (dataset dir name) -> (json file slug prefix, csv "named" column name,
# whether the live route filters to aiNamed>0 & aiEngine, whether it carries a
# namedX list column + tierNote column)
INDUSTRIES = {
    "medspa": {
        "prefix": "medspa",
        "named_count_col": "clinicsNamed",
        "named_list_col": None,
        "has_tier_note": False,
        "filter_named": False,
    },
    "roofers": {
        "prefix": "roofers",
        "named_count_col": "companiesNamed",
        "named_list_col": "namedCompanies",
        "has_tier_note": True,
        "filter_named": True,
    },
    "dentists": {
        "prefix": "dentists",
        "named_count_col": "practicesNamed",
        "named_list_col": "namedPractices",
        "has_tier_note": True,
        "filter_named": True,
    },
    "law-firms": {
        "prefix": "law-firms",
        "named_count_col": "firmsNamed",
        "named_list_col": "namedFirms",
        "has_tier_note": True,
        "filter_named": True,
    },
    "chiropractors": {
        "prefix": "chiropractors",
        "named_count_col": "practicesNamed",
        "named_list_col": "namedPractices",
        "has_tier_note": True,
        "filter_named": True,
    },
    "hvac": {
        "prefix": "hvac",
        "named_count_col": "companiesNamed",
        "named_list_col": "namedCompanies",
        "has_tier_note": True,
        "filter_named": True,
    },
    "plumbers": {
        "prefix": "plumbers",
        "named_count_col": "companiesNamed",
        "named_list_col": "namedCompanies",
        "has_tier_note": True,
        "filter_named": True,
    },
}


def sort_key(c):
    # Biggest markets first, deterministic ties: matches the sort every
    # kkvlabs-landing */data.csv/route.ts and *-data.ts uses.
    return (-c["leads"], -c["checked"], c["city"], c["state"])


def load_cities(prefix):
    with open(LANDING_DATA / f"{prefix}-cities.json") as f:
        return json.load(f)


def write_cities_csv(industry, cfg):
    cities = load_cities(cfg["prefix"])

    if cfg["filter_named"]:
        rows = [c for c in cities if len(c["aiNamed"]) > 0 and c.get("aiEngine")]
    else:
        rows = list(cities)

    rows.sort(key=sort_key)

    columns = ["cityState", "state", "sitesScreened", "noSchema", "noViewport",
               "staleCopyright", cfg["named_count_col"]]
    if cfg["named_list_col"]:
        columns.append(cfg["named_list_col"])
    columns.append("tier")
    if cfg["has_tier_note"]:
        columns.append("tierNote")
    columns.append("aiCheckedOn")

    out_path = REPO_ROOT / "datasets" / industry / "cities.csv"
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        w.writerow(columns)
        for c in rows:
            row = [c["cityState"], c["state"], c["checked"], c["noSchema"],
                   c["noViewport"], c["staleCopyright"], len(c["aiNamed"])]
            if cfg["named_list_col"]:
                row.append("; ".join(c["aiNamed"]))
            row.append(c["tier"])
            if cfg["has_tier_note"]:
                row.append(c.get("tierNote", ""))
            row.append(c["aiCheckedOn"])
            w.writerow(row)
    print(f"wrote {out_path} ({len(rows)} rows)")


SECTION_KEYS = {"name", "label", "sites", "share", "namedShare", "unnamedShare"}


def is_section(value):
    """A stack.json list is a 'section' for stack.csv if every item is a dict
    carrying sites/share/namedShare/unnamedShare and either name or label."""
    if not isinstance(value, list) or not value:
        return False
    for item in value:
        if not isinstance(item, dict):
            return False
        keys = set(item.keys())
        if not {"sites", "share", "namedShare", "unnamedShare"} <= keys:
            return False
        if "name" not in keys and "label" not in keys:
            return False
    return True


META_SCALAR_KEYS = [
    "crawledOn", "sitesAttempted", "sitesRead", "sitesBlocked", "sitesFailed",
    "sitesOffNiche", "namedSites", "unnamedSites", "namedDomainsListed",
]


def write_stack_csv_and_meta(industry, cfg):
    with open(LANDING_DATA / f"{cfg['prefix']}-stack.json") as f:
        stack = json.load(f)

    out_path = REPO_ROOT / "datasets" / industry / "stack.csv"
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        w.writerow(["section", "name", "sites", "share", "namedShare", "unnamedShare"])
        for key, value in stack.items():
            if not is_section(value):
                continue
            for item in value:
                name = item.get("name", item.get("label"))
                w.writerow([key, name, item["sites"], item["share"],
                            item["namedShare"], item["unnamedShare"]])
    print(f"wrote {out_path}")

    meta = {
        "crawledOn": stack.get("crawledOn"),
        "sitesAttempted": stack.get("sitesAttempted"),
        "sitesRead": stack.get("sitesRead"),
        "sitesBlocked": stack.get("sitesBlocked"),
        "namedSites": stack.get("namedSites"),
        "unnamedSites": stack.get("unnamedSites"),
    }
    # carry along any extra crawl-accounting scalars this industry's json has,
    # without inventing fields the json does not carry.
    for k in META_SCALAR_KEYS:
        if k in stack and k not in meta:
            meta[k] = stack[k]

    meta_path = REPO_ROOT / "datasets" / industry / "meta.json"
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
        f.write("\n")
    print(f"wrote {meta_path}")


def main():
    for industry, cfg in INDUSTRIES.items():
        (REPO_ROOT / "datasets" / industry).mkdir(parents=True, exist_ok=True)
        write_cities_csv(industry, cfg)
        write_stack_csv_and_meta(industry, cfg)


if __name__ == "__main__":
    main()
