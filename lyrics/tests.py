import unittest
from lyrics import fetch_lyrics


class TestLyrics(unittest.TestCase):
    def test_fetch_lyrics_returns_string(self):
        self.assertIsInstance(fetch_lyrics('Nirvana', 'In Bloom'), str)
        self.assertIsInstance(fetch_lyrics('Adele', 'Hello'), str)
        self.assertIsInstance(fetch_lyrics('Kendrick Lamar', 'Humble'), str)
        