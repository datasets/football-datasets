"""
Generate pre-aggregated summary CSVs for worldcup Observable Plot views.

Outputs (all written to datasets/worldcup/):
  tournament-goals-summary.csv   — avg goals/game per men's tournament
  goals-by-minute-summary.csv    — goal count per minute (men's, no own goals, min 1–90)
  top-scorers-summary.csv        — top 15 all-time scorers (men's, no own goals)
  tournament-appearances.csv     — number of tournaments each nation appeared in (men's)
"""

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).parent.parent / "datasets" / "worldcup"


def is_mens(row):
    return "Men" in row.get("tournament_name", "")


# ── 1. tournament-goals-summary.csv ─────────────────────────────────────────

def generate_tournament_goals_summary():
    totals = defaultdict(lambda: {"goals": 0, "matches": 0, "tournament_name": ""})

    with open(DATA / "matches.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            if row.get("replayed") == "1":
                continue
            year = row["tournament_id"][3:]  # WC-1930 → 1930
            try:
                goals = int(row["home_team_score"]) + int(row["away_team_score"])
            except (ValueError, KeyError):
                continue
            totals[year]["goals"] += goals
            totals[year]["matches"] += 1
            totals[year]["tournament_name"] = row["tournament_name"]

    rows = []
    for year in sorted(totals):
        t = totals[year]
        if t["matches"] == 0:
            continue
        avg = round(t["goals"] / t["matches"], 2)
        rows.append({"year": year, "tournament_name": t["tournament_name"], "avg_goals_per_game": avg})

    out = DATA / "tournament-goals-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "tournament_name", "avg_goals_per_game"])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


# ── 2. goals-by-minute-summary.csv ──────────────────────────────────────────

def generate_goals_by_minute_summary():
    counts = defaultdict(int)

    with open(DATA / "goals.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            if row.get("own_goal") == "1":
                continue
            try:
                minute = int(row["minute_regulation"])
            except (ValueError, KeyError):
                continue
            if 1 <= minute <= 90:
                counts[minute] += 1

    rows = [{"minute": m, "goal_count": counts[m]} for m in range(1, 91)]

    out = DATA / "goals-by-minute-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["minute", "goal_count"])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} (90 rows)")


# ── 3. top-scorers-summary.csv ───────────────────────────────────────────────

def generate_top_scorers_summary():
    scores = defaultdict(lambda: {"team_name": "", "goals": 0})

    with open(DATA / "goals.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            if row.get("own_goal") == "1":
                continue
            given = row["given_name"] if row["given_name"].lower() != "not applicable" else ""
            player = f"{given} {row['family_name']}".strip()
            scores[player]["goals"] += 1
            scores[player]["team_name"] = row["team_name"]

    ranked = sorted(scores.items(), key=lambda x: x[1]["goals"], reverse=True)[:15]
    rows = [{"player": p, "team_name": v["team_name"], "goals": v["goals"]} for p, v in ranked]

    out = DATA / "top-scorers-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["player", "team_name", "goals"])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


# ── 4. tournament-appearances.csv ────────────────────────────────────────────

def generate_tournament_appearances():
    appearances = defaultdict(set)

    with open(DATA / "team_appearances.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            appearances[row["team_name"]].add(row["tournament_id"])

    rows = sorted(
        [{"team_name": t, "appearances": len(ids)} for t, ids in appearances.items()],
        key=lambda x: x["appearances"],
        reverse=True,
    )

    out = DATA / "tournament-appearances.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["team_name", "appearances"])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


if __name__ == "__main__":
    generate_tournament_goals_summary()
    generate_goals_by_minute_summary()
    generate_top_scorers_summary()
    generate_tournament_appearances()
    print("\nAll summaries generated.")
