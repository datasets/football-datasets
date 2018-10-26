import os
import logging

from dataflows import Flow, update_resource, add_metadata,load, set_type, validate, dump_to_path, printer

import urllib.request, csv
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

base_url = 'http://www.football-data.co.uk/'

readme = 'This dataset contains data for last 10 seasons of %s including current season. The data is updated on weekly basis via Travis-CI. The dataset is sourced from http://www.football-data.co.uk/ website and contains various statistical data such as final and half time result, corners, yellow and red cards etc.'

related_datasets = [
    {
        "title": "English Premier League",
        "path": "/sports-data/english-premier-league",
        "publisher": "sports-data",
        "formats": ["CSV", "JSON"]
    },
    {
        "title": "Spanish La Liga",
        "path": "/sports-data/spanish-la-liga",
        "publisher": "sports-data",
        "formats": ["CSV", "JSON"]
    },
    {
        "title": "German Bundesliga",
        "path": "/sports-data/german-bundesliga",
        "publisher": "sports-data",
        "formats": ["CSV", "JSON"]
    },
    {
        "title": "Italian Serie A",
        "path": "/sports-data/italian-serie-a",
        "publisher": "sports-data",
        "formats": ["CSV", "JSON"]
    },
    {
        "title": "French Ligue 1",
        "path": "/sports-data/french-ligue-1",
        "publisher": "sports-data",
        "formats": ["CSV", "JSON"]
    }
]


licenses = [
    {
      "id": "odc-pddl",
      "path": "http://opendatacommons.org/licenses/pddl/",
      "title": "Open Data Commons Public Domain Dedication and License v1.0",
      'name': "open_data_commons_public_domain_dedication_and_license_v1.0"
    }
]
sources = [
    {
        "name": "www.football-data.co.uk/",
        "path": "http://www.football-data.co.uk/",
        "title": "www.football-data.co.uk/"
    }
]

def get_league_meta(league):
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    req = urllib.request.Request(base_url + league['path'], headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode()
        soup = BeautifulSoup(html, 'html.parser')
        file_links = soup.select('a[href*=mmz4281/]')
        for link in file_links:
            if league['key'] + '.csv' in link['href']:
                league['links'].append(link['href'])
        # Use only last 10 seasons:
        league['links'] = league['links'][:10]
    return league


def get_processors(league):
    processors = []
    for link in league['links']:
        r_name = 'season-' + link.split('/')[-2]
        headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
        processors.append(load(load_source=base_url + link, name=r_name))
        processors.append(update_resource(r_name, **{'path': r_name + '.csv', 'dpp:streaming': True}))
    return processors


def flow(parameters, datapackage, resources, stats):
    meta = get_league_meta(parameters)
    processors = get_processors(meta)
    processors.append(set_type('Date', type='date', format='%d/%m/%y')),
    processors = [add_metadata(
        name=parameters['dataset-name'],
        title=parameters['dataset-title'],
        licenses=licenses,
        sources=sources,
        related=related_datasets,
        readme=readme % parameters['dataset-title'].replace(' (football)', '')
    )] + processors
    return Flow(*processors)


if __name__ == '__main__':
    leagues = [
        {'name': 'premier-league', 'path': 'englandm.php', 'key': 'E0', 'links': [], 'dataset-name': 'english-premier-league', 'dataset-title': 'English Premier League (football)'},
        {'name': 'la-liga', 'path': 'spainm.php', 'key': 'SP1', 'links': [], 'dataset-name': 'spanish-la-liga', 'dataset-title': 'Spanish La Liga (football)'},
        {'name': 'bundesliga', 'path': 'germanym.php', 'key': 'D1', 'links': [], 'dataset-name': 'german-bundesliga', 'dataset-title': 'German Bundesliga (football)'},
        {'name': 'serie-a', 'path': 'italym.php', 'key': 'I1', 'links': [], 'dataset-name': 'italian-serie-a', 'dataset-title': 'Italian Serie A (football)'},
        {'name': 'ligue-1', 'path': 'francem.php', 'key': 'F1', 'links': [], 'dataset-name': 'french-ligue-1', 'dataset-title': 'French Ligue 1 (football)'}
    ]
    for league in leagues:
        meta = get_league_meta(league)
        processors = get_processors(meta)
        processors.append(set_type('Date', type='date', format='%d/%m/%y')),
        processors.append(dump_to_path(out_path='datasets/' + league['name']))
        processors.append(printer())
        processors = [add_metadata(
            name=league['dataset-name'],
            title=league['dataset-title'],
            licenses=licenses,
            sources=sources,
            related=related_datasets,
            readme=readme % league['dataset-title'].replace(' (football)', '')
        )] + processors
        Flow(*processors).process()
