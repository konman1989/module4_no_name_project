import argparse
import json
import requests
from bs4 import BeautifulSoup


def fetch_lyrics(author, song):
    author = author.replace(" ", "-")
    song = song.replace(" ", "-")
    url = f'https://genius.com/{author}-{song}-lyrics'
    result = requests.get(url).text

    soup = BeautifulSoup(result, "html.parser")
    content = soup.find('p').text

    return content


def add_song_text(author, song):

    """If a song exists in json file, adds text in key['Lyrics']"""

    text = fetch_lyrics(author, song)
    with open("../data_base/Database.json", "r") as file:
        content = json.load(file)
        for key in content['data']['Songs']:
            if key['artist'] == author and key['name'] == song:
                key['lyrics'] = text

    with open("../data_base/Database.json", "w") as file1:
        json.dump(content, file1, indent=2)


def to_file(author, song):

    """Checks if the song is already in JSON file, copies song text
    and saves it to a .txt file. If the text does not exist yet,
    parses it, adds to data base and to file"""

    with open("../data_base/Database.json", "r") as file:
        content = json.load(file)
        for key in content['data']['Songs']:
            if key['artist'] == author and key['name'] == song:
                if len(key['lyrics']) > 10:
                    text_to_download = key['lyrics']
            else:
                text_to_download = fetch_lyrics(author, song)
                # if the song is not in DB we save it there
                add_song_text(author, song)

    with open(f"{author}_{song}.txt", "w") as file:
        file.write(f'{text_to_download}')


if __name__ == "__main__":
    to_file('Nirvana', 'In Bloom')
    # to_file('Adele', 'Hello')
    # add_song_text('Adele', 'Hello')
    # add_song_text('Nirvana', 'In Bloom')

    parser = argparse.ArgumentParser()

    parser.add_argument('-a',
                        '--artist',
                        type=str,
                        default=None)
    parser.add_argument('-s',
                        '--song',
                        type=str,
                        default=None)
    parser.add_argument('-f',
                        '--to_file',
                        type=str,
                        default=None)
    parser.add_argument('-d', '--to_db',
                        type=str,
                        default=None)

    args = parser.parse_args()

    # TODO - change parameters in final version to args.