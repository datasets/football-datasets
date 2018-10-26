# Football datasets

This repository includes 5 major Europe leagues:

- English Premier League
- Spanish La Liga
- Italian Serie A
- German Bundesliga
- French Ligue 1

Each league has data for the latest 10 seasons. The data is updated on weekly basis via Travis-CI.

## Data preparation

You need to have Python version >=3.5:

- Install requirements using `pip install -r requirements.txt`
- Run the script `python process.py`

## Packaging datasets

Each directory in `datasets/` directory is a data package. It has a common `schema.json` for all its resources. You need to run `python package.py` from root directory to generate `datapackage.json` for each data package.

## Dataflows

Alternatively you can use dataflows to package the data. Dataflows will do both process the data and prepare datapackage.jsons

```
# Install dataflows
pip install dataflows

# Run flows
python football_data_flow.py
```
