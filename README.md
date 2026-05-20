<a className="gh-badge" href="https://datahub.io/football"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Football datasets

This repository includes 5 major Europe leagues and a World Cup dataset:

- English Premier League – https://datahub.io/football/english-premier-league
- Spanish La Liga – https://datahub.io/football/spanish-la-liga
- Italian Serie A – https://datahub.io/football/italian-serie-a
- German Bundesliga – https://datahub.io/football/german-bundesliga
- French Ligue 1 – https://datahub.io/football/french-ligue-1
- FIFA World Cup – https://datahub.io/football/worldcup

Each league has data for all the seasons. The data is updated on a daily basis via GitHub Actions.

## Data

The data is sourced from the `https://www.football-data.co.uk/` website, datasets range starts from 1993 up to current year.

## Preparation

You need to have Python version >=3.5:

- Install requirements using `pip install -r scripts/requirements.txt`
- Fetch and process league data: `python scripts/process.py`
- Generate datapackage.json for each dataset: `python scripts/package.py`

## Automation

Up-to-date (auto-updates every day) football dataset could be found on the datahub.io: https://datahub.io/football/football-datasets

## Packaging datasets

Each directory in `datasets/` directory is a data package. It has a common `schema.json` for all its resources. You need to run `python scripts/package.py` from the root directory to generate `datapackage.json` for each data package.

## License

The league datasets are made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/

The World Cup dataset is derived from the [Fjelstul World Cup Database](https://github.com/jfjelstul/worldcup) and is published under the [Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/) license. Attribution: Joshua C. Fjelstul, Ph.D.
