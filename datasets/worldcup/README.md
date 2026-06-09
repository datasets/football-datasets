Comprehensive data on every FIFA World Cup tournament — men's (1930–2022) and women's (1991–2019) — covering matches, goals, squads, bookings, penalty shootouts, awards, and more. Sourced from the [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) by Joshua C. Fjelstul, Ph.D.

## Dataset Overview

27 interlinked CSV tables spanning the full history of the World Cup, from Uruguay 1930 to Qatar 2022.

**Coverage**

- Men's: all 22 tournaments (1930–2022), 900+ matches, 3,600+ goals
- Women's: all 8 tournaments (1991–2019)

**Updated** automatically whenever the upstream Fjelstul database is updated.

## Derived summary tables

Alongside the 27 core Fjelstul tables, the package ships small **pre-aggregated summary tables** (men's tournaments only) that power the charts and data stories:

| Resource | What it covers |
|----------|----------------|
| `tournament-goals-summary` | Average goals per game, by tournament (1930–2022) |
| `goals-by-minute-summary` | Goals scored at each match minute (1–90), all tournaments |
| `top-scorers-summary` | Top 15 all-time men's World Cup scorers |
| `tournament-appearances` | Top 20 nations by tournaments played |
| `goal-timing-by-tournament-summary` | Stoppage-time goals, share of goals in stoppage time, and average goal minute, by tournament (1930–2022) |
| `discipline-by-tournament-summary` | Yellow/red cards and cards per match, by tournament (1970–2022, since cards were introduced) |
| `dirtiest-matches-summary` | The 15 most-carded matches in men's World Cup history |

The goal-timing and discipline tables are derived directly from the `goals` and `bookings` resources; regenerating them needs only those source tables.

## License

This dataset is derived from the [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) and is published under the [Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

**Attribution:** Joshua C. Fjelstul, Ph.D. — © 2023 Joshua C. Fjelstul, Ph.D.

You are free to share and adapt this data for any purpose as long as you provide proper attribution and distribute any derivative works under the same license.
