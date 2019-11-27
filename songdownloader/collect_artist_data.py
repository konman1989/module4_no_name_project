import argparse
import json
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Last.fm_bio')
parser.add_argument(
    '-a',
    '--artist',
    type=str,
    help='no artist'
)

args = parser.parse_args()
response = requests.get(f'https://www.last.fm/music/{args.artist}').text
soup = BeautifulSoup(response, "html.parser")
table = soup.find('div', {'class': 'metadata-column'})
try:
    bday = table.findAll('dd')[0].text
    bplace = table.findAll('dd')[1].text
except AttributeError:
    bday = None
    bplace = None
    print('Sorry, no information')


with open(f'bio{args.artist}.json', 'w') as file:
    json_data = []
    json_data.append({
            'name': args.artist,
            'born/founded': bday,
            'born in/founded in': bplace
    })

    file.write(json.dumps(json_data, indent=2))
