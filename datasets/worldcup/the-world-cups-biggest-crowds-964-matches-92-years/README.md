# The World Cup's Biggest Crowds — 964 Matches, 92 Years

Data story for the **`attendance`** resource of the `worldcup` dataset.

- **[STORY.mdx](STORY.mdx)** — the full narrative with the embedded interactive chart, methodology and caveats.
- **Data:** the [`../attendance.csv`](../attendance.csv) resource (964 per-match rows, 1930–2022), defined in [`../datapackage.json`](../datapackage.json).

The chart is a modular `<VegaLite spec={chartSpec} />` MDX component; it loads `../attendance.csv` via `spec.data.url` and aggregates to a per-edition average on the fly.
