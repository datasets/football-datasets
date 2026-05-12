import glob, json, copy


dpjson_template = {
    "name": "",
    "title": "",
    "description": "",
    "resources": [],
    "licenses": [
        {
            "name": "ODC-PDDL-1.0",
            "path": "https://opendatacommons.org/licenses/pddl/",
            "title": "Open Data Commons Public Domain Dedication and License"
        }
    ],
    "sources": [
        {
            "name": "Football-Data.co.uk",
            "path": "https://www.football-data.co.uk/",
            "title": "Football-Data.co.uk"
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
        "title": "English Premier League (football)",
        "description": "Match results for every English Premier League season from 1993/94 to present, including full-time and half-time scores, referee, shots, corners, fouls, and cards. Updated daily. Source: Football-Data.co.uk."
    },
    "la-liga": {
        "name": "spanish-la-liga",
        "title": "Spanish La Liga (football)",
        "description": "Match results for every Spanish La Liga season from 1993/94 to present, including full-time and half-time scores, referee, shots, corners, fouls, and cards. Updated daily. Source: Football-Data.co.uk."
    },
    "bundesliga": {
        "name": "german-bundesliga",
        "title": "German Bundesliga (football)",
        "description": "Match results for every German Bundesliga season from 1993/94 to present, including full-time and half-time scores, referee, shots, corners, fouls, and cards. Updated daily. Source: Football-Data.co.uk."
    },
    "serie-a": {
        "name": "italian-serie-a",
        "title": "Italian Serie A (football)",
        "description": "Match results for every Italian Serie A season from 1993/94 to present, including full-time and half-time scores, referee, shots, corners, fouls, and cards. Updated daily. Source: Football-Data.co.uk."
    },
    "ligue-1": {
        "name": "french-ligue-1",
        "title": "French Ligue 1 (football)",
        "description": "Match results for every French Ligue 1 season from 1993/94 to present, including full-time and half-time scores, referee, shots, corners, fouls, and cards. Updated daily. Source: Football-Data.co.uk."
    }
}


def season_label(resource_name):
    """Convert a season resource name like 'season-9394' to a human label like '1993/94'."""
    code = resource_name.replace("season-", "")
    s, e = int(code[:2]), code[2:]
    start = (1900 + s) if s >= 60 else (2000 + s)
    return f"{start}/{e}"


league_dirs = glob.glob('datasets/*')

for league_dir in league_dirs:
    dpjson = copy.deepcopy(dpjson_template)
    league_name = league_dir.split('/')[1]
    dpjson['name'] = leagues[league_name]['name']
    dpjson['title'] = leagues[league_name]['title']
    dpjson['description'] = leagues[league_name]['description']
    with open(league_dir + '/schema.json') as schema:
        schema = json.load(schema)
        resources = sorted(glob.glob(league_dir + '/*.csv'), reverse=True)
        for resource in resources:
            resource = resource.split('/')[-1]
            descriptor = copy.deepcopy(resource_descriptor)
            descriptor['path'] = resource
            descriptor['name'] = resource.replace('.csv', '')
            label = season_label(descriptor['name'])
            descriptor['description'] = f"{leagues[league_name]['title'].split(' (')[0]} season {label} match results."
            descriptor['schema'] = copy.deepcopy(schema)
            dpjson['resources'].append(descriptor)
        # Add related datasets:
        for dataset in related_datasets:
            if dataset['path'].split('/')[-1] != dpjson['name']:
                dpjson['related'].append(dataset)
        with open(league_dir + '/datapackage.json', 'w') as dp:
            json.dump(dpjson, dp, indent=2)
