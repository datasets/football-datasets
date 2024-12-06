<a className="gh-badge" href="https://datahub.io/core/football-datasets"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

# Football datasets

This repository includes 5 major Europe leagues:

- English Premier League
- Spanish La Liga
- Italian Serie A
- German Bundesliga
- French Ligue 1

Each league has data for the all the seasons. The data is updated on monthly basis via Github-Actions

## Data
    The data is sourced from the `https://www.football-data.co.uk/` website, datasets range starts from 1993 up to current year

## Preparation

You need to have Python version >=3.5:

- Install requirements using `pip install -r scripts/requirements.txt`
- Run the script `python scripts/process.py`
- Update datapackage `pyhton scripts/process.py`

## Automation

Up-to-date (auto-updates every month) football dataset could be found on the datahub.io: https://datahub.io/core/football-datasets

## Packaging datasets

Each directory in `datasets/` directory is a data package. It has a common `schema.json` for all its resources. You need to run `python package.py` from root directory to generate `datapackage.json` for each data package.

## License

This Data Package is made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/