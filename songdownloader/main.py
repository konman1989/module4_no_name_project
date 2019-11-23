import argparse
import json
import requests

parser = argparse.ArgumentParser(description='ITunes parser')
parser.add_argument(
    '-a',
    '--artist',
    type=str,
    help='no artist'
)
parser.add_argument(
    '-l',
    '--limit',
    type=int,
    default=2
)
parser.add_argument(
    '-c',
    '--country',
    type=str,
    help='no county',
    default=None
)


args = parser.parse_args()

if len(args.country) != 2:
    raise NameError("Country length should equal 2")

response = requests.get(f"https://itunes.apple.com/search?term={args.artist}&"
                        f"country={args.country}&limit={args.limit}").json()

with open(f'{args.artist}.json', 'w') as file:
    json_data = []
    for char in response['results']:
        json_data.append({
            'artist': char["artistName"],
            'song': char["trackName"],
            'genre': char["primaryGenreName"],
            'country': char["country"],
            'trackExplicitness': char["trackExplicitness"],
            'artWorkUrl': char["artworkUrl100"]
        })

    file.write(json.dumps(json_data, indent=2))
