import unittest
from src import Room, Guest, Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(name="Blue", guest_limit=3)
        self.song1 = Song("With a Little Help from My Friends", "The Beatles")
        self.song2 = Song("Lucy in the Sky with Diamonds", "The Beatles")

    def test_room_has_name(self):
        self.assertEqual("Blue", self.room.name)

    def test_room_has_guest_limit(self):
        self.assertEqual(3, self.room.guest_limit)

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_add_one_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song1)
        self.assertEqual([self.song1], self.room.playlist)

    def test_add_two_songs_to_playlist(self):
        self.room.add_song_to_playlist(self.song1)
        self.room.add_song_to_playlist(self.song2)
        self.assertEqual(self.song2, self.room.playlist[1])

    def test_clear_playlist(self):
        self.room.add_song_to_playlist(self.song1)
        self.room.add_song_to_playlist(self.song2)
        self.assertEqual(2, len(self.room.playlist))
        self.room.clear_playlist()
        self.assertEqual(0, len(self.room.playlist))

    @unittest.skip("Room guests not implemented yet")
    def test_room_is_empty(self):
        self.assertTrue(self.room.is_empty())

    @unittest.skip("Room guests not implemented yet")
    def test_add_guest__guest_has_paid(self):
        self.room.add_guest(self.guest_paid)
        self.assertFalse(self.room.is_empty())

    @unittest.skip("Room guests not implemented yet")
    def test_add_guest__guest_not_paid(self):
        self.room.add_guest(self.guest_not_paid)
        self.assertTrue(self.room.is_empty())

    @unittest.skip("Room guests not implemented yet")
    def test_clear_guests(self):
        self.room.add_guest(self.guest_paid)
        self.assertFalse(self.room.is_empty())
        self.room.clear_guests()
        self.assertTrue(self.room.is_empty())