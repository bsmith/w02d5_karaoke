import unittest
from src import KaraokeBar, Room, Guest, Song

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(name="Blue", guest_limit=3)
        self.room2 = Room(name="Red", guest_limit=10)
        self.room3 = Room(name="Yellow", guest_limit=5)
        self.rooms = [self.room1, self.room2, self.room3]
        self.guests = [Guest(f"Test Guest #{n+1}", 50) for n in range(6)]
        self.karaoke_bar = KaraokeBar(self.rooms, 25)

    @unittest.skip("Not implemented")
    def test_bar_has_rooms(self):
        self.assertEqual(3, len(self.karaoke_bar.rooms))

    @unittest.skip("Not implemented")
    def test_bar_has_entrance_fee(self):
        self.assertEqual(25, self.karaoke_bar.entrance_fee)

    @unittest.skip("Not implemented")
    def test_bar_has_zero_takings(self):
        self.assertEqual(0, self.karaoke_bar.takings)

    @unittest.skip("Not implemented")
    def test_find_empty_room__one_guest(self):
        empty_room = self.karaoke_bar.find_empty_room(1)
        self.assertEqual(self.room1, empty_room)

    @unittest.skip("Not implemented")
    def test_find_empty_room__four_guests(self):
        empty_room = self.karaoke_bar.find_empty_room(4)
        self.assertIn([self.room2, self.room3], empty_room)

    @unittest.skip("Not implemented")
    def test_find_empty_room__twelve_guests(self):
        empty_room = self.karaoke_bar.find_empty_room(12)
        self.assertIsNone(empty_room)

    @unittest.skip("Not implemented")
    def test_increase_takings(self):
        self.karaoke_bar.increase_takings(50);
        self.assertEqual(self.karaoke_bar.takings, 50)

    @unittest.skip("Not implemented")
    def test_check_in_guests__room_with_space(self):
        self.karaoke_bar.check_in_guests(self.room3, self.guests[0:3])
        self.assertEqual(3, len(self.room3.guests))
        self.assertTrue(all([guest.paid_fee for guest in self.guests[0:3]]))
        self.assertEqual(25 * 3, self.karaoke_bar.takings)

    @unittest.skip("Not implemented")
    def test_check_in_guests__room_with_no_space(self):
        self.karaoke_bar.check_in_guests(self.room3, self.guests)
        self.assertEqual(0, len(self.room3.guests))
        self.assertTrue(all([not guest.paid_fee for guest in self.guests]))
        self.assertEqual(0, self.karaoke_bar.takings)

    @unittest.skip("Not implemented")
    def test_check_in_guests__guest_cannot_pay(self):
        poor_guest = Guest("Guest #7", 1)
        self.karaoke_bar.check_in_guests(self.room1, [poor_guest])
        self.assertTrue(self.room1.is_empty())
        self.assertFalse(poor_guest.paid_fee)
        self.assertEqual(0, self.karaoke_bar.takings)

    @unittest.skip("Not implemented")
    def test_check_out_guests(self):
        self.karaoke_bar.check_in_guests(self.room3, self.guests)
        self.karaoke_bar.check_out_guests(self.room3)
        self.assertTrue(self.room3.is_empty())
