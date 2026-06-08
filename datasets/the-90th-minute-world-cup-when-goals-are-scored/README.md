# The 90th-Minute World Cup — When Goals Are Actually Scored

The `worldcup` dataset knows the exact minute of all **2,720 goals** scored across the
men's World Cup. The **`goal-timing-by-tournament-summary` resource** rolls them up
edition by edition — and the timeline tells a clear story: **World Cup goals keep
arriving later and later in the match.**

## The headline number

In the modern, fully-timed era (**1990–2022**), **114 of 1,392 goals — 8.2% — were
scored in stoppage time.** More than one in twelve. The single most dramatic edition was
**Russia 2018: 13.0% of all goals came after the 90th (or 45th) minute.**

## Goals are creeping later in the game

The average minute of a World Cup goal has drifted **from ~48 at mid-century into the
mid-50s in the modern era — 55.7 in 2022.** (The single latest-scoring edition on record
is actually low-scoring **Italy 1990 at 59.3**, when goals were scarce and often came
late.) Late drama isn't a vibe; it's in the data:

- **2022:** average goal minute **55.7**, **12.2%** of goals in stoppage time.
- **2018:** **53.7** average minute, **13.0%** in stoppage — the highest share on record.
- **1998:** the first edition where stoppage goals broke double digits — **11.1%**.

## The honest caveat (read this before quoting the chart)

The source assigns an explicit **added-time minute only from 1990 onward**. Every goal
before 1990 is recorded with a stoppage value of `0`. That does **not** mean nobody ever
scored in added time before 1990 — they did. It means the database doesn't tag *which*
pre-1990 goals fell in stoppage, so the share is unmeasurable, not zero. **The
stoppage-time series is therefore scoped to 1990–2022.** The `avg_goal_minute` and
`goals_per_match` columns are reliable across all 22 tournaments.

## While we're here: the goals themselves

Goals per match peaked long ago — **Switzerland 1954 at 5.38 per game** — and have
settled into a tight modern band around **2.5–2.7**. Qatar 2022 landed at **2.69**, the
highest since 2014. The game didn't get less prolific so much as more *evenly spread*:
fewer blowouts, more goals arriving in the final fifteen.

## What's in the resource

One row per men's World Cup (1930–2022): matches, total goals (own goals included, so it
reconciles with the match tables), goals per match, regulation vs. stoppage goals, the
share of goals in stoppage time, and the average goal minute. Derived directly from the
`goals` resource — regenerating it needs only that table.

## Sources
- **Fjelstul World Cup Database** — the men's World Cup `goals` table (minute of every goal).
