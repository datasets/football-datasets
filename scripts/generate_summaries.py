"""
Generate pre-aggregated summary CSVs for worldcup Observable Plot views.

Outputs (all written to datasets/worldcup/):
  tournament-goals-summary.csv           — avg goals/game per men's tournament
  goals-by-minute-summary.csv            — goal count per minute (men's, no own goals, min 1–90)
  top-scorers-summary.csv                — top 15 all-time scorers (men's, no own goals)
  tournament-appearances.csv             — number of tournaments each nation appeared in (men's)
  goal-timing-by-tournament-summary.csv  — regulation/stoppage goal split per men's tournament
  discipline-by-tournament-summary.csv   — cards per men's tournament (since cards introduced)
  dirtiest-matches-summary.csv           — 15 most-carded men's matches
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

    # minute_start/end used by rectY (linear x scale, avoids band scale issue)
    rows = [{"minute_start": m - 1, "minute_end": m, "goal_count": counts[m]} for m in range(1, 91)]

    out = DATA / "goals-by-minute-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["minute_start", "minute_end", "goal_count"])
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
    )[:20]

    out = DATA / "tournament-appearances.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["team_name", "appearances"])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


# ── 5. goal-timing-by-tournament-summary.csv ─────────────────────────────────

def generate_goal_timing_by_tournament_summary():
    # match count per men's tournament (includes replayed matches)
    matches = defaultdict(int)
    with open(DATA / "matches.csv") as f:
        for row in csv.DictReader(f):
            if is_mens(row):
                matches[row["tournament_id"]] += 1

    stats = defaultdict(lambda: {"name": "", "goals": 0, "stoppage": 0, "minute_sum": 0, "minute_n": 0})
    with open(DATA / "goals.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            t = stats[row["tournament_id"]]
            t["name"] = row["tournament_name"]
            t["goals"] += 1
            try:
                stoppage = int(row["minute_stoppage"])
            except (ValueError, KeyError):
                stoppage = 0
            if stoppage > 0:
                t["stoppage"] += 1
            try:
                regulation = int(row["minute_regulation"])
            except (ValueError, KeyError):
                regulation = None
            if regulation is not None:
                t["minute_sum"] += regulation + stoppage
                t["minute_n"] += 1

    rows = []
    for tid in sorted(stats):
        t = stats[tid]
        m, g = matches[tid], t["goals"]
        rows.append({
            "year": tid.split("-")[1],
            "tournament_name": t["name"],
            "matches": m,
            "goals": g,
            "goals_per_match": round(g / m, 2),
            "regulation_goals": g - t["stoppage"],
            "stoppage_goals": t["stoppage"],
            "pct_goals_in_stoppage": round(t["stoppage"] / g * 100, 1),
            "avg_goal_minute": round(t["minute_sum"] / t["minute_n"], 1),
        })

    out = DATA / "goal-timing-by-tournament-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "year", "tournament_name", "matches", "goals", "goals_per_match",
            "regulation_goals", "stoppage_goals", "pct_goals_in_stoppage", "avg_goal_minute",
        ])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


# ── 6. discipline-by-tournament-summary.csv ──────────────────────────────────
# Only covers tournaments present in bookings.csv (cards introduced in 1970).
# total_cards = yellow_cards + straight_red_cards: a second yellow is already
# counted as a yellow, so the resulting red is not an extra physical card.

def generate_discipline_by_tournament_summary():
    matches = defaultdict(int)
    with open(DATA / "matches.csv") as f:
        for row in csv.DictReader(f):
            if is_mens(row):
                matches[row["tournament_id"]] += 1

    stats = defaultdict(lambda: {"name": "", "yellow": 0, "second_yellow": 0, "straight_red": 0})
    with open(DATA / "bookings.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            t = stats[row["tournament_id"]]
            t["name"] = row["tournament_name"]
            t["yellow"] += row["yellow_card"] == "1"
            t["second_yellow"] += row["second_yellow_card"] == "1"
            if row["red_card"] == "1" and row["second_yellow_card"] != "1":
                t["straight_red"] += 1

    rows = []
    for tid in sorted(stats):
        t = stats[tid]
        m = matches[tid]
        red = t["straight_red"] + t["second_yellow"]
        total = t["yellow"] + t["straight_red"]
        rows.append({
            "year": tid.split("-")[1],
            "tournament_name": t["name"],
            "matches": m,
            "yellow_cards": t["yellow"],
            "second_yellow_cards": t["second_yellow"],
            "straight_red_cards": t["straight_red"],
            "red_cards": red,
            "total_cards": total,
            "cards_per_match": round(total / m, 2),
        })

    out = DATA / "discipline-by-tournament-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "year", "tournament_name", "matches", "yellow_cards", "second_yellow_cards",
            "straight_red_cards", "red_cards", "total_cards", "cards_per_match",
        ])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


# ── 7. dirtiest-matches-summary.csv ──────────────────────────────────────────

def generate_dirtiest_matches_summary():
    matches = defaultdict(lambda: {
        "tournament_id": "", "match_name": "", "stage_name": "", "match_date": "",
        "yellow": 0, "second_yellow": 0, "straight_red": 0,
    })
    with open(DATA / "bookings.csv") as f:
        for row in csv.DictReader(f):
            if not is_mens(row):
                continue
            m = matches[row["match_id"]]
            m["tournament_id"] = row["tournament_id"]
            m["match_name"] = row["match_name"]
            m["stage_name"] = row["stage_name"]
            m["match_date"] = row["match_date"]
            m["yellow"] += row["yellow_card"] == "1"
            m["second_yellow"] += row["second_yellow_card"] == "1"
            if row["red_card"] == "1" and row["second_yellow_card"] != "1":
                m["straight_red"] += 1

    ranked = []
    for m in matches.values():
        red = m["straight_red"] + m["second_yellow"]
        total = m["yellow"] + m["straight_red"]
        ranked.append((total, red, m))
    # most cards first; ties broken by more red cards, then earlier match date
    ranked.sort(key=lambda r: (-r[0], -r[1], r[2]["match_date"]))

    rows = []
    for total, red, m in ranked[:15]:
        year = m["tournament_id"].split("-")[1]
        rows.append({
            "year": year,
            "tournament_name": f"{year} FIFA Men's World Cup",
            "match_name": m["match_name"],
            "stage_name": m["stage_name"],
            "match_date": m["match_date"],
            "yellow_cards": m["yellow"],
            "red_cards": red,
            "total_cards": total,
        })

    out = DATA / "dirtiest-matches-summary.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "year", "tournament_name", "match_name", "stage_name", "match_date",
            "yellow_cards", "red_cards", "total_cards",
        ])
        w.writeheader()
        w.writerows(rows)
    print(f"✓ {out.name} ({len(rows)} rows)")


def main():
    generate_tournament_goals_summary()
    generate_goals_by_minute_summary()
    generate_top_scorers_summary()
    generate_tournament_appearances()
    generate_goal_timing_by_tournament_summary()
    generate_discipline_by_tournament_summary()
    generate_dirtiest_matches_summary()
    print("\nAll summaries generated.")


if __name__ == "__main__":
    main()
