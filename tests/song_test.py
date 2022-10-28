import unittest
from dataclasses import FrozenInstanceError
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Sgt. Pepper's Lonely Hearts Club Band", "The Beatles")
    
    def test_song_has_title(self):
        self.assertEqual("Sgt. Pepper's Lonely Hearts Club Band", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("The Beatles", self.song.artist)

    def test_song_is_frozen(self):
        def try_changing_title():
            self.song.title = "Eleanor Rigby"
        def try_changing_artist():
            self.song.artist = "Paul McCartney"
        self.assertRaises(FrozenInstanceError, try_changing_title)
        self.assertRaises(FrozenInstanceError, try_changing_artist)