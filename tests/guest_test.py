import unittest
from src.guest import Guest
from src.caraoke_bar import CaraokeBar
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.caraoke_bar = CaraokeBar("Code Clan Caraoke",100)
        self.room_1 = Room("Hello Kitty",2)
        self.room_2 = Room("My Little Pony",5)
        self.caraoke_bar.rooms = [self.room_1, self.room_2]
        self.song_1 = Song("YMCA", "The Village People")
        self.song_2 = Song("Eye of the Tiger","Survivor")
        self.caraoke_bar.music_librairy = [self.song_1, self.song_2]
        self.guest_1 = Guest("Arnold Schwarzenegger",self.caraoke_bar)
        self.guest_2 = Guest("Sylvester Stallone",self.caraoke_bar)
        self.guest_3 = Guest("Jackie Chan",self.caraoke_bar)
        self.guest_4 = Guest("Chris Tucker",self.caraoke_bar)

    def test_guest_has_name_Arnold_Schwarzenegger(self):
        self.assertEqual("Arnold Schwarzenegger", self.guest_1.guest_name)


    def test_guest_has_name_Sylvester_Stallone(self):
        self.assertEqual("Sylvester Stallone", self.guest_2.guest_name)

    
