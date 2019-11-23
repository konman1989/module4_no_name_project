import requests
import json


def fetch_artist(name: str):
    result = requests.get(
        f"https://api.genius.com/search?q={name}",
        headers={
            'Authorization':
                'Bearer wVnMu7TSGw3HDXdeRmWuQUWOHgoIBC9L-Z6Sb7ehJf3NPippFG5D7YWJSsm3z6kY'
        }).json()

    for songs in result['response']:
        print(songs)

    return json.dumps(result, indent=2)



print(fetch_artist('eminem'))

# https://api.genius.com/search?q={name}"