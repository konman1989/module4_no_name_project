import unittest
from lyrics import fetch_lyrics, to_file


class TestLyrics(unittest.TestCase):
    def test_fetch_lyrics_returns_string(self):
        self.assertIsInstance(fetch_lyrics('Nirvana', 'In Bloom'), str)
        self.assertIsInstance(fetch_lyrics('Adele', 'Hello'), str)
        self.assertIsInstance(fetch_lyrics('Kendrick Lamar', 'Humble'), str)

    def test_to_file_creates_txt_file_and_downloads_content(self):
        text_to_check = fetch_lyrics('Nirvana', 'In Bloom')
        to_file('Nirvana', 'In Bloom')

        with open('Nirvana_In Bloom.txt', 'r') as file:
            text_from_file = file.read()

        self.assertEqual(text_to_check, text_from_file)

