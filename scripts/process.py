import re
import os
import csv
import chardet
import datetime
import requests
import urllib.request

from bs4 import BeautifulSoup
from user_agent import generate_user_agent

BASE_URL = 'https://www.football-data.co.uk/'
COLUMNS_ORDER = [
    "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", 
    "HTHG", "HTAG", "HTR", "Referee", "HS", "AS", "HST", 
    "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"
]

LEAGUES = [
    {'name': 'premier-league', 'path': 'englandm.php', 'key': 'E0', 'links': [], 'range': 23},
    {'name': 'la-liga', 'path': 'spainm.php', 'key': 'SP1', 'links': [], 'range': 22},
    {'name': 'bundesliga', 'path': 'germanym.php', 'key': 'D1', 'links': [], 'range': 22},
    {'name': 'serie-a', 'path': 'italym.php', 'key': 'I1', 'links': [], 'range': 22},
    {'name': 'ligue-1', 'path': 'francem.php', 'key': 'F1', 'links': [], 'range': 22}
]

def fetch_league_links(league):
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    response = requests.get(BASE_URL + league['path'], headers=headers, verify=False)  # Disable SSL verification
    soup = BeautifulSoup(response.text, 'html.parser')
    file_links = soup.find_all('a', href=re.compile(r"mmz4281"))
    for link in file_links:
        if league['key'] + '.csv' in link['href']:
            league['links'].append(link['href'])

def download_and_save_data(league):
    """Download data from league links and save in specified format."""
    for link in league['links']:
        headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
        req = urllib.request.Request(BASE_URL + link, headers=headers)
        with urllib.request.urlopen(req) as response:
            header = True
            raw_data = response.read()
            # Detect encoding
            detected_encoding = chardet.detect(raw_data)['encoding']
            if not detected_encoding:
                raise ValueError("Failed to detect encoding for the file.")
            
            # Decode using detected encoding
            data = raw_data.decode(detected_encoding)
            save_dir = f'datasets/{league["name"]}'
            os.makedirs(save_dir, exist_ok=True)
            path_to_save = f'{save_dir}/season-{link.split("/")[-2]}.csv'
            with open(path_to_save, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                reader = csv.DictReader(data.splitlines())
                # Write reordered header
                writer.writerow(COLUMNS_ORDER)
                for row in reader:
                    if row["Date"] and row["Date"].strip():
                        date_parts = row["Date"].split("/")
                        if len(date_parts) == 3 and int(date_parts[2]) >= 1900:
                            x = datetime.datetime(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
                            row["Date"] = x.strftime('%d/%m/%y')
                        # Write the reordered row
                        reordered_row = [row.get(col, "") for col in COLUMNS_ORDER]
                        writer.writerow(reordered_row)

def main():
    """Main function to fetch and process league data."""
    for league in LEAGUES:
        fetch_league_links(league)
        download_and_save_data(league)

if __name__ == "__main__":
    main()
