# The Dirtiest World Cups — 50 Years of Yellow and Red

Yellow and red cards didn't exist until the **1970 World Cup**, where referees brandished
just **52 cards in 32 matches**. The **`discipline-by-tournament-summary` resource**
tracks every booking since — and it pinpoints exactly when the World Cup got mean, and
when it cooled back down.

## The headline number

The angriest tournament ever played was **Germany 2006: 5.23 cards per match** — **335
cards across 64 games**, including 28 sending-offs. No edition before or since has come
close to that rate.

## The arc: from polite to brutal and back

- **1970** — cards introduced. **1.62 per match.** Referees are still feeling it out.
- **1990–2006** — the hard-tackling era. The rate climbs from 3.44 (1990) through 4.54
  (1994) and peaks at **5.23 in 2006**.
- **2014–2022** — the cool-down. **2014 drops to 2.98**, and the last two editions sit
  around **3.5** — roughly two cards a game below the 2006 peak.

What changed after 2006 wasn't player temperament so much as refereeing instruction and
broadcast scrutiny: consistent thresholds, more managed games, fewer mass-booking
flashpoints.

## Reds are rarer than the totals suggest

The `red_cards` column counts every dismissal — **second yellows plus straight reds** (the
two add up exactly). 2006 also tops the red-card chart with **28 dismissals**; by contrast
the disciplined recent editions logged just **4 reds each in 2018 and 2022**, despite
playing the same 64 matches. Cards went up, then players learned to stay on the pitch.

## What's in the resource

One row per men's World Cup from **1970 to 2022** (the card era): matches, yellow cards,
second yellows, straight reds, total dismissals, total cards, and cards per match. Derived
directly from the `bookings` resource. Pre-1970 tournaments are intentionally absent —
there were no cards to count.

## Going deeper

For the individual flashpoints behind these averages — the single most-carded matches in
World Cup history — see the companion story
[**The 15 Most-Carded Matches in World Cup History**](../the-15-most-carded-matches-in-world-cup-history/),
built from the `dirtiest-matches-summary` resource.

## Sources
- **Fjelstul World Cup Database** — the men's World Cup `bookings` table (every yellow and
  red card, with match and player).
