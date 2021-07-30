import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room
from src.caraoke_bar import CaraokeBar

class TestCaraokeBar(unittest.TestCase):
    
    def setUp(self):
        self.caraoke_bar = CaraokeBar("Code Clan Caraoke")
        self.room_1 = Room("Hello Kitty")
        self.guest_1 = Guest("Arnold Schwarzenegger")
        self.guest_2 = Guest("Sylvester Stallone")

    def test_caraoke_bar_has_name_Code_Clan_Caraoke(self):
        self.assertEqual("Code Clan Caraoke", self.caraoke_bar.caraoke_bar_name)
    
    def test_check_in_guest_into_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.assertEqual(1, self.room_1.check_number_of_occupants())

    def test_check_in_two_guests_into_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_1)
        self.assertEqual(2, self.room_1.check_number_of_occupants())

