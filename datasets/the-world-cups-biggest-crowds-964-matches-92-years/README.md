# The World Cup's Biggest Crowds — 964 Matches, 92 Years

The Fjelstul match tables in the `worldcup` dataset record every men's World Cup match
ever played — but not a single attendance figure. The **`attendance` resource** fills
that gap: **all 964 men's matches from Uruguay 1930 to Qatar 2022, each with the crowd
that watched it.**

## The trend, edition by edition
Averaged per match across each men's World Cup from 1930 to 2022, attendance climbed
through the early decades and then settled into a band. **USA 1994 (68,991 per match)
is still the record.** Totals rose as the tournament expanded, but the per-edition
average is flatter — peaking in 1994 and bouncing between ~42,000 and ~53,000 in the
64-match era.

## The headline number

Across 92 years and 964 matches, the men's World Cup has been watched in stadiums by
**43.9 million spectators**.

## The all-time record still belongs to 1950

The single largest crowd in World Cup history was **173,850**, at the
**Maracanã in Rio de Janeiro on 16 July 1950** — Uruguay 2–1 Brazil, the *Maracanazo*,
the match that decided the 1950 World Cup. The four biggest crowds ever recorded are
*all* from that 1950 tournament at the Maracanã. No match since has come close; the
modern stadium-capacity era (and all-seater safety rules) capped what's possible.

## But the biggest *tournament* was USA 1994

Per match, the best-attended World Cup ever was **United States 1994: 68,991 average**,
from a total of **3.59 million** — and it did that with only **52 matches**, before the
field expanded to 32 teams. Three decades later, 1994 still holds both the average and
total records. For comparison:

- **Lowest average:** France 1938 — 20,872 per match (17 matches, knockout-only format).
- **Qatar 2022:** 53,191 average / 3.40 million total across 64 matches.
- **The expansion effect:** totals climbed as the tournament grew from 18 matches (1930)
  to 64 (1998–2022), but *average* attendance is flatter — peaking in 1994 and bouncing
  between ~42,000 and ~53,000 in the 64-match era.

## What's in the resource

- **[`attendance.csv`](../worldcup/attendance.csv)** — one row per match: `year`, `stage`, `phase`, `date`, both teams,
  `score`, `attendance`, `stadium`, `city`, and a per-row `source`. Joins to the match
  tables (e.g. `matches.csv`) on `(year, teams, date)`.

## How it was built & validated

Attendance is not in the Fjelstul database, so it was assembled from two sources and
**cross-checked against an independent reference** before inclusion:

| Editions | Source | Validation result |
|---|---|---|
| 1930–2010 (19 editions) | Kaggle/FIFA `WorldCupMatches` | Per-tournament averages match the independent `fifa-stats` reference **to the exact person (0.0%)** |
| 2014 | Wikipedia match reports | Within **1.3%** of the reference (announced match-day figures) |
| 2018, 2022 | Wikipedia match reports | Tournament totals match FIFA's official figures **exactly** (3,031,768 and 3,404,252) |

Two matches absent from the Wikipedia knockout wikitext (the 2014 Germany 7–1 Brazil
semifinal and the 2022 Netherlands–Argentina quarter-final) were sourced individually
and are flagged in the `source` column. The per-match `source` column records provenance
for every row.

## Caveats

- **Scope is men's only** — the `attendance` resource covers the 964 men's matches; women's
  World Cup attendance is not included here.
- **2014–2022 use announced match-day attendance** (as reported by Wikipedia/FIFA);
  FIFA occasionally revises figures, which is why 2014 sits 1.3% from the older reference.
- **Historical team names are preserved** (West Germany, Yugoslavia, Soviet Union).
- The `score` column is full-time/AET as recorded; penalty-shootout results are not
  encoded separately.

Full dataset notes: [`worldcup/README.md`](../worldcup/README.md).
