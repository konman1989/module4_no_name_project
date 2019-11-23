import argparse
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


print(fetch_lyrics('Kendrick Lamar', 'Humble'))

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--artist', type=str, default=None)
parser.add_argument('-s', '--song', type=str, default=None)
parser.add_argument('-f', '--to_file', type=str, default=None)
parser.add_argument('-d', '--to_db', type=str, default=None)

args = parser.parse_args()


def to_file(artist, song, path):
    with open(f'{path}/{artist}_{song}.txt', "w") as file:
        file.write(f'{artist}\n{fetch_lyrics(artist, song)}')


to_file(args.artist, args.song, args.to_file)


# def to_db(author, song, song_id):
#     return fetch_lyrics()



