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
    ]
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
    dpjson = dict(dpjson_template)
    dpjson['resources'] = []
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
            if league_name == 'ligue-1' and resource == 'season-1819.csv':
                for field in descriptor['schema']['fields']:
                    if field['name'] == 'HF':
                        field['name'] = 'HFKC'
                        field['description'] = 'Home Team Free Kicks Conceded'
                    elif field['name'] == 'AF':
                        field['name'] = 'AFKC'
                        field['description'] = 'Away Team Free Kicks Conceded'
            dpjson['resources'].append(descriptor)
            with open(league_dir + '/datapackage.json', 'w') as dp:
                json.dump(dpjson, dp, indent=2)
