import datetime
import urllib.request, csv
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

base_url = 'http://www.football-data.co.uk/'
leagues = [
    {'name': 'premier-league', 'path': 'englandm.php', 'key': 'E0', 'links': [], 'range': 23},
    {'name': 'la-liga', 'path': 'spainm.php', 'key': 'SP1', 'links': [], 'range': 22},
    {'name': 'bundesliga', 'path': 'germanym.php', 'key': 'D1', 'links': [], 'range': 22},
    {'name': 'serie-a', 'path': 'italym.php', 'key': 'I1', 'links': [], 'range': 22},
    {'name': 'ligue-1', 'path': 'francem.php', 'key': 'F1', 'links': [], 'range': 22}
]

for league in leagues:
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    req = urllib.request.Request(base_url + league['path'], headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode()
        soup = BeautifulSoup(html, 'html.parser')
        file_links = soup.select('a[href*=mmz4281]')
        for link in file_links:
            if league['key'] + '.csv' in link['href']:
                league['links'].append(link['href'])
        # Use only last 10 seasons:
        league['links'] = league['links'][:10]
    for link in league['links']:
        headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
        req = urllib.request.Request(base_url + link, headers=headers)
        with urllib.request.urlopen(req) as response:
            header = True
            data = response.read().decode()
            path_to_save = 'datasets/' + league['name'] + '/season-' + link.split('/')[-2] + '.csv'
            with open(path_to_save, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                reader = csv.reader(data.splitlines())
                for row in reader:
                    if header:
                        writer.writerow(row[1:int(league['range'])])
                        header = False
                        continue
                    if row[1] != '':
                        date = row[1].split("/")
                        if int(date[2]) >= 1900:
                            x = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
                            row[1] = x.strftime('%d/%m/%y')
                        writer.writerow(row[1:int(league['range'])])
