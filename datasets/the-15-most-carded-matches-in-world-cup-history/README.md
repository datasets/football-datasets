# The 15 Most-Carded Matches in World Cup History

Some World Cup matches stop being football. The referee runs out of patience, the cards
pile up, and a quarter-final turns into a brawl with a scoreline attached.

We ranked the **15 most-carded matches in men's World Cup history** — every yellow and red
pinned to the exact game it came out in. These are the nights the game got away from
everyone.

## The record: a referee loses control of a quarter-final

**Netherlands 2, Argentina 2 — Qatar 2022, 9 December.** Fifteen cards. One match.

Antonio Mateu Lahoz lost the thread of a tie that would go to penalties, and the bookings
just kept coming until he'd shown more cards than any referee in the 92-year history of
the tournament. **The single most-carded game ever played.**

## The worst of the worst

| Match | Tournament | Stage | Cards |
|-------|------------|-------|------:|
| Netherlands vs Argentina | 2022 | Quarter-final | **15** |
| Cameroon vs Germany | 2002 | Group stage | 14 |
| Netherlands vs Spain | 2010 | **Final** | 13 |
| Portugal vs Netherlands | 2006 | Round of 16 | 12 |
| Senegal vs Uruguay | 2002 | Group stage | 12 |

## The one that crashed a final

Most of these wars happen early, when the stakes are low and the tempers high. **2010 was
different.** The **Netherlands–Spain final** at Soccer City ran up **13 cards** — the
dirtiest final the World Cup has ever staged, the night Nigel de Jong planted his studs in
Xabi Alonso's chest and somehow stayed on the field. A showpiece occasion. A bloodbath.

## About that "Battle of Nuremberg"

You've heard that **Portugal vs Netherlands, 2006**, was the match where referee Valentin
Ivanov "showed 16 cards." This dataset records **12, with 4 dismissals** — and we'll take
the source over the legend. Different counters tally second yellows and the post-whistle
bookings their own way; we trust the `bookings` table rather than inflate the number to
fit the myth. Even at 12, it's the most red-soaked game in the top five.

## How we count

`total_cards` = yellows **+** straight reds. A second yellow is already a yellow, so it's
never double-counted — which is why a genuinely vicious match can post a smaller total than
its reputation. The separate `red_cards` column counts **dismissals** (second yellows plus
straight reds), so you can see exactly how many players actually walked.

## What's in the data

Fifteen rows, one per match: year, tournament, fixture, stage, date, yellows, reds, and
total cards — ranked on unique match IDs, so repeat fixtures across tournaments never
collide. Built from the `bookings` and `matches` resources.

## Source
- **Fjelstul World Cup Database** — the men's `bookings` and `matches` tables.
