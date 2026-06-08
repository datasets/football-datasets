# The 15 Most-Carded Matches in World Cup History

Some World Cup matches stop being football and become crime scenes. The
**`dirtiest-matches-summary` resource** ranks the **15 most-carded men's World Cup
matches ever**, drawn from the full `bookings` table — every yellow and red, keyed to the
exact match it was shown in.

## The headline number

The record holder is **Netherlands 2–2 Argentina, Qatar 2022 quarter-final
(9 December 2022): 15 cards in one match.** Referee Antonio Mateu Lahoz lost control of a
tie that went to penalties, and the bookings just kept coming — the single most-carded
game in 92 years of World Cup football.

## The top of the table

| Match | Tournament | Stage | Total cards |
|-------|------------|-------|-------------|
| Netherlands vs Argentina | 2022 | Quarter-final | **15** |
| Cameroon vs Germany | 2002 | Group stage | 14 |
| Netherlands vs Spain | 2010 | **Final** | 13 |
| Portugal vs Netherlands | 2006 | Round of 16 | 12 |
| Senegal vs Uruguay | 2002 | Group stage | 12 |

## The one that got into a final

Most blood-and-thunder games happen early, when the stakes are lower and the tempers
shorter. **Not in 2010.** The **Netherlands–Spain final** at Soccer City logged **13
cards** — the dirtiest World Cup final ever, defined by Nigel de Jong's studs-up challenge
on Xabi Alonso's chest. A final is supposed to be the showpiece; this one is in the
all-time top three for cards.

## A note on the "Battle of Nuremberg"

**Portugal vs Netherlands, 2006 round of 16**, is infamous as the match where referee
Valentin Ivanov "showed 16 cards." This dataset records it at **12 cards (with 4
dismissals)** — and we report the source figure, not the legend. Different counters tally
second yellows and the famous post-final-whistle bookings differently; we trust the
Fjelstul `bookings` table rather than inflating the number to match the myth. It's still
the most red-card-heavy game in the top five.

## How the count works

`total_cards` = yellow cards **+** straight reds. A second yellow is already counted as a
yellow, so it isn't double-counted — which is why a match can show fewer `total_cards`
than its drama suggests. The separate `red_cards` column counts **dismissals** (second
yellows + straight reds), so you can see how many players actually walked.

## What's in the resource

15 rows, one per match: year, tournament, match name, stage, date, yellow cards, red
cards (dismissals), and total cards. Ranked on unique match IDs — not match names — so
repeat fixtures across tournaments never collide. Derived directly from the `bookings` and
`matches` resources.

## Sources
- **Fjelstul World Cup Database** — the men's World Cup `bookings` and `matches` tables.
