import glob, json, copy


dpjson_template = {
    "name": "",
    "title": "",
    "resources": [],
    "licenses": [
        {
            "name": "ODC-PDDL",
            "path": "http://opendatacommons.org/licenses/pddl/",
            "title": "Open Data Commons Public Domain Dedication and License"
        }
    ],
    "sources": [
        {
            "name": "www.football-data.co.uk/",
            "path": "http://www.football-data.co.uk/",
            "title": "www.football-data.co.uk/"
        }
    ],
    "related": []
}

resource_descriptor = {
    "name": "",
    "path": "",
    "format": "csv",
    "mediatype": "text/csv",
    "encoding": "ISO-8859-1",
    "dialect": {
        "delimiter": ",",
        "quoteChar": "\""
    }
}

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

leagues = {
    "premier-league": {
        "name": "english-premier-league",
        "title": "English Premier League (football)"
    },
    "la-liga": {
        "name": "spanish-la-liga",
        "title": "Spanish La Liga (football)"
    },
    "bundesliga": {
        "name": "german-bundesliga",
        "title": "German Bundesliga (football)"
    },
    "serie-a": {
        "name": "italian-serie-a",
        "title": "Italian Serie A (football)"
    },
    "ligue-1": {
        "name": "french-ligue-1",
        "title": "French Ligue 1 (football)"
    }
}

league_dirs = glob.glob('datasets/*')

for league_dir in league_dirs:
    dpjson = copy.deepcopy(dpjson_template)
    league_name = league_dir.split('/')[1]
    dpjson['name'] = leagues[league_name]['name']
    dpjson['title'] = leagues[league_name]['title']
    with open(league_dir + '/schema.json') as schema:
        schema = json.load(schema)
        resources = sorted(glob.glob(league_dir + '/*.csv'), reverse=True)
        for resource in resources:
            resource = resource.split('/')[-1]
            descriptor = copy.deepcopy(resource_descriptor)
            descriptor['path'] = resource
            descriptor['name'] = resource.replace('.csv', '')
            descriptor['schema'] = copy.deepcopy(schema)
            dpjson['resources'].append(descriptor)
        # Add related datasets:
        for dataset in related_datasets:
            if dataset['path'].split('/')[-1] != dpjson['name']:
                dpjson['related'].append(dataset)
        with open(league_dir + '/datapackage.json', 'w') as dp:
            json.dump(dpjson, dp, indent=2)
