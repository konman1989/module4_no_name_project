import argparse
import json
import requests
from bs4 import BeautifulSoup


import data_base as db


def fetch_lyrics(author, song):
    author = author.replace(" ", "-")
    song = song.replace(" ", "-")
    url = f'https://genius.com/{author}-{song}-lyrics'
    result = requests.get(url).text

    soup = BeautifulSoup(result, "html.parser")

    content = soup.find('p').text

    return content


# print(fetch_lyrics('Kendrick Lamar', 'Humble'))

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--artist', type=str, default=None)
parser.add_argument('-s', '--song', type=str, default=None)
parser.add_argument('-f', '--to_file', type=str, default=None)
parser.add_argument('-d', '--to_db', type=str, default=None)

args = parser.parse_args()


def to_file(artist, song, path):
    with open(f'{path}/{artist}_{song}.txt', "w") as file:
        file.write(f'{artist}\n{fetch_lyrics(artist, song)}')

def text_to_db(author, song):
    # text = fetch_lyrics(author, song)
    with open("Database.json", "r") as file:
        text = json.loads(file)
    print(text)

text_to_db('a', 'b')
# to_file(args.artist, args.song, args.to_file)


# content = fetch_lyrics('Nirvana', 'In bloom')

DB1 = db.DataBase()

table = db.Table('Lyrics', DB1)
table.add_parameter('id', 'int')
table.add_parameter('text', 'str')
table.add_parameter('song_id', 'id')






# table.add_to_table()
# DB1.to_json()
#
# lyrics = db.Table('Lyrics', db.DB)