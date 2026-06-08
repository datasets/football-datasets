# The Dirtiest World Cups

For the first forty years of the World Cup, a referee had no card to show you. Then came
**1970** — yellows and reds arrive — and the tournament hands out a grand total of **52
cards in 32 matches.** Polite. Restrained. It would not last.

We tracked every booking from that day to Qatar 2022, and the chart has a clear villain
and a clear redemption arc.

## The meanest tournament ever played

**Germany 2006.** Five-point-two-three cards a match. **335 in total, 28 of them
dismissals** — a tournament so fractious that one round-of-16 tie alone produced four red
cards. No World Cup before or since has come close to that rate. If you want a single
number for "peak nastiness," it's **5.23.**

## How the game got mean — then calmed down

- **1970** — cards introduced. **1.62 a match.** Referees still finding the holster.
- **1990–2006** — the hatchet era. The rate climbs from 3.44, through 4.54 at USA '94, and
  tops out at **5.23 in 2006.**
- **2014–2022** — the cool-down. **2014 collapses to 2.98**, and the last two editions
  settle near **3.5** — a full two cards a game below the 2006 peak.

What changed wasn't the players' tempers. It was the officiating: clearer thresholds,
relentless broadcast scrutiny, and referees coached to manage a game instead of papering
it in yellow.

## Players learned to stay on the pitch

The `red_cards` column counts dismissals — second yellows and straight reds, which add up
exactly. 2006 tops that chart too, with **28 players sent off.** Fast-forward to the
disciplined modern editions and **2018 and 2022 logged just 4 reds each** — across the
same 64 matches. The cards kept coming; the early showers stopped.

## Want the individual crime scenes?

The averages hide the flashpoints. For the single most-carded matches in World Cup
history — the night a referee lost the Netherlands and Argentina entirely, the dirtiest
final ever played — read the companion piece:
[**The 15 Most-Carded Matches in World Cup History**](../the-15-most-carded-matches-in-world-cup-history/).

## What's in the data

One row per men's World Cup, **1970 to 2022** — the entire card era: matches, yellows,
second yellows, straight reds, total dismissals, total cards, and cards per match. Built
straight from the `bookings` resource. There are no pre-1970 rows because there were no
cards to count.

## Source
- **Fjelstul World Cup Database** — the men's `bookings` table, every yellow and red.
