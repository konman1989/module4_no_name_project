import argparse
import requests
import json
from bs4 import BeautifulSoup


def fetch_lyrics(author, song):
    author = author.replace(" ", "-")
    song = song.replace(" ", "-")
    url = f'https://genius.com/{author}-{song}-lyrics'
    result = requests.get(url).text

    soup = BeautifulSoup(result, "html.parser")

    content = soup.find('p').text

    return content


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--artist', type=str, default=None)
parser.add_argument('-s', '--song', type=str, default=None)
parser.add_argument('-f', '--to_file', type=str, default=None)
parser.add_argument('-d', '--to_db', type=str, default=None)

args = parser.parse_args()


def to_file(author, song, path):

    """Checks if the song is already in JSON file, copies song text
    and saves it to a .txt file. If the text does not exist yet,
    parses it, adds to data base and to file"""

    with open("Database.json", "r") as file:
        content = json.load(file)
        for key in content['data']['Songs']:
            if key['artist'] == author and key['name'] == song:
                if key['Lyrics'] != 'text':
                    text_to_download = key['Lyrics']
            else:
                text_to_download = fetch_lyrics(author, song)

    with open(f'{path}/{author}_{song}.txt', "w") as file:
        file.write(f'{author}\n{text_to_download}')


if __name__ == "__main__":
    to_file('Nirvana', 'In Bloom', '')
    to_file('Adele', 'Hello', '')