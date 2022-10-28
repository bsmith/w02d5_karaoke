import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(name="Blue", guest_limit=3)

    def test_room_has_name(self):
        self.assertEqual("Blue", self.room.name)

    def test_room_has_guest_limit(self):
        self.assertEqual(3, self.room.guest_limit)

    def test_room_has_empty_playlist(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room.guests))
