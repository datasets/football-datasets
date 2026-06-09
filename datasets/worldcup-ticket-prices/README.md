# FIFA World Cup Final Ticket Prices per Edition (1994–2026)

The most expensive (**Category-1**) World Cup **final** ticket, face value, nominal USD, one row
per edition — plus the 2026 price tiers. The 2026 final tops out at **$10,990 face value (6.8× the
2022 price)**, with resale near **$33,000** and a **$60 "Supporter Entry" floor**; the pricing drew
a **subpoena of FIFA by the NY & NJ attorneys general (27 May 2026)**.

## Data

### `ticket_prices.csv` — one row per edition

| field | type | description |
|-------|------|-------------|
| year | integer | edition year (1994–2026) |
| host | string | host nation(s) |
| cat1_final_usd_nominal | number | most expensive final ticket, face value, nominal USD (blank where unavailable) |
| status | string | face_value / face_value_approx / DISPUTED_likely_resale / missing |
| source | string | citation |

### `ticket_2026_tiers.csv`
2026 tiers: $60 entry → $5,785 Cat-3 → $10,990 Cat-1 (face value) → ~$32,970 resale.

## ⚠️ Data-quality note (THIN dataset — read this)
- **Gaps:** 1998 and 2006 have **no reliable primary** face-value source — left **blank, not interpolated**.
- **Disputed:** the widely-cited 2014 ≈ $6,000 looks like **resale**, not face value — flagged in `status`, exclude from trends.
- **Nominal, not inflation-adjusted:** in real terms pre-2026 finals were roughly flat (~$1,300 in 2026 USD); the clean low-inflation comparison is **2018 → 2022 → 2026**. The 2026 jump holds in real terms regardless.

## Sources
- SI.com (per-edition prices, cites Statista + FIFA); NY/NJ Attorneys General press release (the probe, primary); FIFA (2026 tiers). World Bank CPI (CC-BY 4.0) can be used for inflation adjustment.

## License
Figures are factual; reuse **with attribution**. AG press release is public domain.
