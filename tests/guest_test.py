import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest(name="Grace", wallet=50.0)

    def test_guest_has_name(self):
        self.assertEqual("Grace", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50.0, self.guest.wallet)
    
    def test_guest_has_not_paid_fee_yet(self):
        self.assertFalse(self.guest.paid_fee)

    @unittest.skip("Fees and affordability not implemented yet")
    def test_guest_can_afford_fee__True(self):
        pass

    @unittest.skip("Fees and affordability not implemented yet")
    def test_guest_can_afford_fee__False(self):
        pass

    @unittest.skip("Fees and affordability not implemented yet")
    def test_guest_pay_fee__affordable(self):
        pass

    @unittest.skip("Fees and affordability not implemented yet")
    def test_guest_pay_fee__unaffordable(self):
        pass