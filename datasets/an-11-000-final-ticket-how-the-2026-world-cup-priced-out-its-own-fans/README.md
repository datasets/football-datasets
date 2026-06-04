# An $11,000 final ticket: how the 2026 World Cup priced out its own fans
*For three decades a World Cup final seat ran in the hundreds to low thousands. In 2026 it hit five figures — and two attorneys general want to know why.*

**The insight:** The most expensive (Category-1) **2026 final** ticket is **$10,990 face value** — **6.8× the 2022 price ($1,607)** and far beyond any prior edition. Resale listings peaked near **$32,970**; the cheapest "Supporter Entry" seat is **$60** (a small allotment). On **May 27 2026**, the New York & New Jersey attorneys general **subpoenaed FIFA** over variable (dynamic) pricing after **>90 of 104 matches** rose by an **average 34%**.

**Why now:** the AG subpoena is days old (May 27 2026) and the tournament kicks off June 11 — the story is live.

## Each edition, with its gaps shown
Tracked across editions, the most expensive (Category-1) final ticket — face value, nominal USD — was flat in the hundreds-to-low-thousands range for decades before spiking in 2026. Two editions are genuine gaps with no reliable primary source (**1998** and **2006**), and they are left as gaps rather than interpolated. **2014's** widely-cited ~$6,000 figure is disputed (likely a resale price) and is excluded from the trend. The clean, low-inflation comparison is **2018 → 2022 → 2026**, and that is where the jump to $10,990 stands out.

## Data & provenance
- **Data files:** [`ticket_prices.csv`](../worldcup-ticket-prices/ticket_prices.csv) (per-edition Cat-1 final, each figure status-flagged) + [`ticket_2026_tiers.csv`](../worldcup-ticket-prices/ticket_2026_tiers.csv).
- **Sources:** [SI.com](https://www.si.com/soccer/how-outrageous-ticket-prices-for-2026-world-cup-final-compare-to-past-years) (per-edition, cites Statista+FIFA); [NY/NJ AG press release](https://ag.ny.gov/press-release/2026/attorney-general-james-and-attorney-general-davenport-subpoena-fifa-over-world) (**primary** — the probe); [FIFA](https://inside.fifa.com/news/world-cup-2026-new-ticket-pricing-tier-fans-qualified-teams) ($60 tier); [The World Cup Guide](https://theworldcupguide.com/how-much-are-world-cup-tickets-since-1994/) (real-terms). *Why:* no single dataset exists, so the well-sourced 2026 figures + the primary AG probe carry the story; older editions add context with flags.
- **Lineage:** journalism + AG release + FIFA → `ticket_prices.csv` (status column flags face-value / disputed / missing). Full dataset notes: [`worldcup-ticket-prices/README.md`](../worldcup-ticket-prices/README.md).

**Caveat (data is THIN):** prices are **nominal** (not inflation-adjusted); in real terms pre-2026 finals were roughly flat (~$1,300 in 2026 dollars). 1998/2006 are genuine gaps; **2014 is disputed** (likely resale). The unprecedented 2026 level holds regardless — even 1994's ~$1,500 nominal (~$3,200 real) is a fraction of $10,990.

**Source:** SI.com; NY/NJ Attorneys General (May 27 2026); FIFA; The World Cup Guide. Figures cited with attribution.

**Post copy:** "A 2026 World Cup final ticket: $10,990 face value — 6.8× the 2022 price, with resale near $33k. Two US attorneys general just subpoenaed FIFA over it. ⚽️💸 #WorldCup2026"
