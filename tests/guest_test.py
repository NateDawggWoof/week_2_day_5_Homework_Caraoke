import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    # def setUp(self): 
    #     self.guest = PGuest()

    def test_guest_has_name_Arnold_Schwarzenegger(self):
        guest_1 = Guest("Arnold Schwarzenegger")
        self.assertEqual("Arnold Schwarzenegger", guest_1.guest_name)

