import unittest
from lyrics.lyrics import fetch_lyrics, to_file, add_song_text
from data_base.main import DataBase


class TestLyrics(unittest.TestCase):
    def test_fetch_lyrics_returns_string(self):
        self.assertIsInstance(fetch_lyrics('Nirvana', 'In Bloom'), str)
        self.assertIsInstance(fetch_lyrics('Adele', 'Hello'), str)
        self.assertIsInstance(fetch_lyrics('Kendrick Lamar', 'Humble'), str)

    def test_to_file_creates_txt_file_and_downloads_content(self):
        text_to_check = fetch_lyrics('Nirvana', 'In Bloom')
        to_file('Nirvana', 'In Bloom', 'Nirvana_In_Bloom.txt')

        with open('Nirvana_In_Bloom.txt', 'r') as file_:
            text_from_file = file_.read()

        self.assertEqual(text_to_check, text_from_file)

    def test_add_song_text_returns_empty_list_if_artist_not_in_db(self):
        value = add_song_text('Nirvanana', 'In Rotten')

        self.assertIsInstance(value, list)

    def test_add_song_text_adds_text_in_DB_if_missing(self):
        add_song_text('Nirvana', 'In Bloom')
        value = DataBase.select('Songs', artist='Nirvana', name='In Bloom')
        self.assertTrue(len(value[0]['lyrics']) > 10)

        value2 = DataBase.select('Songs', artist='Adele', name='Hello')
        self.assertTrue(len(value2[0]['lyrics']) < 10)

        add_song_text('Adele', 'Hello')
        value3 = DataBase.select('Songs', artist='Adele', name='Hello')
        self.assertTrue(len(value3[0]['lyrics']) > 10)
