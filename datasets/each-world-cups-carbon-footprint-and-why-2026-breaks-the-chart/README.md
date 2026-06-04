# Each World Cup's carbon footprint — and why 2026 breaks the chart
*The 2026 finals are projected at ~9 million tonnes of CO₂ — and the data shows why: a continent-sized, three-nation tournament runs on flights.*

**The insight:** On a like-for-like basis, 2026 is projected at **9.0 Mt CO₂e — about +92% above the recalculated 2010–2022 average (4.71 Mt)** — and **~86% of it (7.72 Mt) is air travel**. It tops even the expanded 2030 (6.1 Mt) and 2034 (8.6 Mt) editions.

**Why now:** kicks off **June 11, 2026** across the US, Canada and Mexico — the first 48-team, 104-match, three-nation finals.

## Reading the data — two sources, one honest comparison
Two different measurements sit behind this story, and they are **not** on the same scale:
- **2010–2022 (each host's own report):** South Africa **2.75**, Brazil **2.27**, Russia **2.16**, Qatar **3.63** Mt. These use FIFA's narrower accounting boundary.
- **2026–2034 (SGR's independent projections):** computed on a **fuller** scope — and SGR recalculates the 2010–22 average at **4.71 Mt** on that same scope.

So the honest comparison is **2026 (9.0) vs the recalculated 4.71 average — both on the fuller scope → +92%.** Comparing the 2026 projection straight to the older self-reported figures would *overstate* the jump, because those self-reports undercount (SGR's central argument: FIFA self-reports leave out most aviation — which is exactly why the historical figures sit *below* the recalculated average).

Put plainly: the per-edition figures span South Africa 2010 through the projected 2034 tournament. The earlier editions reflect each host's own FIFA-scope report; the 2026–2034 editions reflect SGR's fuller-scope projections. The two scopes are not directly comparable — read the 2026 figure against the recalculated 4.71 Mt average, not against the older bars.

## Data & provenance
- **Data files:** [`emissions_per_edition.csv`](../worldcup-carbon-footprint/emissions_per_edition.csv) (7 tournaments — host, Mt, and which methodology) + [`emissions_reference.csv`](../worldcup-carbon-footprint/emissions_reference.csv) (SGR recalc average; 2026 air/other split).
- **Sources:** [SGR / New Weather Institute, *FIFA's Climate Blind Spot* (2025)](https://www.sgr.org.uk/publications/fifa-s-climate-blind-spot-men-s-world-cup-warming-world) — attribution; the only independent projection for the 3-nation 2026 tournament. [FIFA host sustainability audits via Play the Game](https://www.playthegame.org/themes/sport-and-climate-change/understanding-sports-carbon-emissions/) — public reporting; the per-edition history. *Why both:* one gives consistent forward projections, the other gives the per-country past.
- **Lineage:** FIFA host audits (self-report scope) + SGR 2025 (projections + recalc average, fuller scope) → combined into `emissions_per_edition.csv` with a `basis` column flagging each row's methodology. Full dataset notes: [`worldcup-carbon-footprint/README.md`](../worldcup-carbon-footprint/README.md).

**Caveat:** 2026/2030/2034 are projections; the historical figures use a narrower scope than the projections — presented together to show each tournament, **not** to be subtracted from one another. Use the SGR like-for-like average for the headline comparison. The 7.72 Mt air-travel figure is from **SGR Table ES-1** (primary report), independently re-verified against the source PDF.

**Post copy:** "Every World Cup's carbon footprint, by host — and 2026 breaks the chart. ~9 Mt CO₂, +92% vs the comparable recent average, and 86% is just flights between three host nations. ✈️🌍 #WorldCup2026"
