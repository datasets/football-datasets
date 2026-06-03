# $42 Million to Win, $9 Million to Show Up — and a 4x Gender Gap

The `worldcup` dataset tells you who won. This one tells you what it paid.

## What each team takes home

FIFA splits the World Cup prize pool by how far you go. At **Qatar 2022**, that meant:

| Finish | Teams | Each earned |
|---|---:|---:|
| Winner | 1 | **$42M** |
| Runner-up | 1 | $30M |
| Third place | 1 | $27M |
| Fourth place | 1 | $25M |
| Quarter-finals (5th–8th) | 4 | $17M |
| Round of 16 (9th–16th) | 8 | $13M |
| Group stage (17th–32nd) | 16 | $9M |

Argentina's $42M down to $9M for each of the 16 teams that went home after the group
stage. **Those 32 cheques add up to exactly $440 million** — the published prize pool.
That's the validation built into this dataset: in `prize_by_team.csv`, every edition's
per-team payouts sum to the official pool to the dollar (2010 $348M, 2014 $358M,
2018 $400M, 2022 $440M).

## The winner's cheque keeps growing

| Edition | Winner gets | Total pool |
|---|---:|---:|
| 2010 South Africa | $30M | $348M |
| 2014 Brazil | $35M | $358M |
| 2018 Russia | $38M | $400M |
| 2022 Qatar | $42M | $440M |
| 2026 USA/CAN/MEX | **$50M** | $655M |

2026 is the big jump — a 48-team field, a $655M pool, and a brand-new **Round-of-32**
payout band (see `prize_schedule.csv`). Each schedule sums to its pool too:
50+33+29+27 + 19×4 + 15×8 + 11×16 + 9×16 = $655M.

## The gap the money exposes

Put the men's and women's prize pools on the same axis (`prize_pool_by_edition.csv`)
and the story is stark:

- The **2022 men's pool was $440M**. The **2023 women's pool was $110M** — a **4-to-1 gap**.
- Women's World Cup prize money was **$0 until 2007**, then $5.8M (2007) → $30M (2019)
  → $110M (2023).
- FIFA has committed to **prize-money parity by 2027** — which is why the women's 2027
  row is a placeholder (target announced, figure to be confirmed).

## How it was built

- **Payout schedules** (per position, per edition): FIFA announcements, compiled via
  topendsports and contemporaneous reporting.
- **Who finished where:** top-four placements from FIFA final standings; every other
  team's bracket derived from its furthest stage in the **Fjelstul World Cup Database**
  match data (e.g. a team whose deepest match was a Round-of-16 loss → 9th–16th band).
- **Self-check:** per-team sums reconciled against the published pool for every edition
  (all four match exactly).

## Caveats

- **Per-team rows cover men's 2010–2022** (editions with both a published schedule and
  results). 2026 is schedule-only — no results yet.
- **Pre-2014 men's pool figures are FIFA *total contribution*** (broader scope including
  preparation/club payments), not directly comparable to 2014+ prize-money-proper
  figures — flagged in the `note` column and worth keeping in mind when reading the trend.
- The women's series here is **per-edition totals**; per-team women's payouts (which mix
  team and individual-player components) are a planned extension.
- All figures are **nominal USD** — not inflation-adjusted.
