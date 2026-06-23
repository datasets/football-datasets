import os
import requests

from generate_summaries import main as generate_summaries

BASE_URL = "https://raw.githubusercontent.com/jfjelstul/worldcup/master/data-csv"

TABLES = [
    "tournaments",
    "teams",
    "players",
    "managers",
    "referees",
    "stadiums",
    "confederations",
    "awards",
    "host_countries",
    "qualified_teams",
    "groups",
    "tournament_stages",
    "matches",
    "goals",
    "bookings",
    "penalty_kicks",
    "substitutions",
    "squads",
    "group_standings",
    "tournament_standings",
    "team_appearances",
    "player_appearances",
    "manager_appearances",
    "manager_appointments",
    "referee_appearances",
    "referee_appointments",
    "award_winners",
]


def main():
    out_dir = "datasets/worldcup"
    os.makedirs(out_dir, exist_ok=True)

    for table in TABLES:
        url = f"{BASE_URL}/{table}.csv"
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        path = os.path.join(out_dir, f"{table}.csv")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(r.text)
        lines = r.text.count("\n")
        print(f"  {table}: {lines} rows")

    # Regenerate the derived summary tables from the freshly downloaded data so
    # they never drift out of sync with the upstream Fjelstul database.
    print("Regenerating summary tables...")
    generate_summaries()


if __name__ == "__main__":
    main()
