Comprehensive data on every FIFA World Cup tournament — men's (1930–2022) and women's (1991–2019) — covering matches, goals, squads, bookings, penalty shootouts, awards, and more. Sourced from the [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) by Joshua C. Fjelstul, Ph.D.

## Dataset Overview

27 interlinked CSV tables spanning the full history of the World Cup, from Uruguay 1930 to Qatar 2022.

**Coverage**
- Men's: all 22 tournaments (1930–2022), 900+ matches, 3,600+ goals
- Women's: all 8 tournaments (1991–2019)

**Updated** automatically whenever the upstream Fjelstul database is updated.

## Tables

### Core match data
| File | Rows | Description |
|---|---|---|
| `tournaments.csv` | 30 | One row per tournament — host, winner, format, dates |
| `matches.csv` | 1,248 | Results with FT, HT, ET, and penalty shootout scores |
| `goals.csv` | 3,637 | Every goal: scorer, minute, penalty/own-goal flags |
| `bookings.csv` | 3,178 | Yellow and red cards |
| `penalty_kicks.csv` | 396 | Individual kicks in shootouts with outcome |
| `substitutions.csv` | 10,222 | Player substitutions with minute |

### Players & squads
| File | Rows | Description |
|---|---|---|
| `players.csv` | 10,401 | Master list of all World Cup players |
| `squads.csv` | 13,843 | Squad registration per tournament (position, shirt number, club) |
| `player_appearances.csv` | 27,432 | Player per match — starter, position, minutes played |

### People
| File | Description |
|---|---|
| `managers.csv` | All World Cup managers |
| `manager_appointments.csv` | Manager per tournament |
| `manager_appearances.csv` | Manager per match |
| `referees.csv` | All World Cup referees |
| `referee_appointments.csv` | Referee per tournament |
| `referee_appearances.csv` | Referee per match |

### Standings & awards
| File | Description |
|---|---|
| `group_standings.csv` | P/W/D/L/GF/GA/Pts per team per group |
| `tournament_standings.csv` | Final standings per tournament |
| `award_winners.csv` | Golden Boot, Golden Ball, Golden Glove, Best Young Player, Fair Play |
| `awards.csv` | Award type reference |

### Reference
| File | Description |
|---|---|
| `teams.csv` | National teams with confederation |
| `stadiums.csv` | Venues with city, country, and capacity |
| `confederations.csv` | FIFA confederations |
| `host_countries.csv` | Host countries per tournament |
| `qualified_teams.csv` | Teams per tournament |
| `groups.csv` | Groups per tournament |
| `tournament_stages.csv` | Stages per tournament |
| `team_appearances.csv` | Team per match with goals and result |

## Key Fields

**matches.csv** — `tournament_id`, `match_date`, `stage_name`, `group_name`, `home_team_name`, `away_team_name`, `home_team_score`, `away_team_score`, `extra_time`, `penalty_shootout`, `home_team_score_penalties`, `away_team_score_penalties`, `result`

**goals.csv** — `tournament_name`, `match_date`, `team_name`, `given_name`, `family_name`, `minute_regulation`, `minute_stoppage`, `match_period`, `own_goal`, `penalty`

**squads.csv** — `tournament_name`, `team_name`, `given_name`, `family_name`, `position_name`, `shirt_number`

## Example Analyses

- **Top scorers all time**: aggregate goals per player across all tournaments (Miroslav Klose leads with 16)
- **Goals by match minute**: group by `minute_regulation` to reveal the spike at 45' and 90' stoppage time
- **Host nation advantage**: join `tournaments.csv` with `host_countries.csv` — hosts have won 6 of 22 tournaments
- **Card trends over time**: group `bookings.csv` by tournament to see the 2006 Germany spike (28 red cards)
- **Penalty shootout pressure**: analyse conversion rate by kick order in `penalty_kicks.csv`
- **Squad age over time**: compute average player age from `squads.csv` by tournament

## License

This dataset is derived from the [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) and is published under the [Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license.

**Attribution:** Joshua C. Fjelstul, Ph.D. — © 2023 Joshua C. Fjelstul, Ph.D.

You are free to share and adapt this data for any purpose as long as you provide proper attribution and distribute any derivative works under the same license.
