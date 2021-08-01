import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.caraoke_bar import CaraokeBar

class TestSong(unittest.TestCase):
    
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

    def test_song_has_song_name_Eye_Of_The_Tiger(self):
        song_1 = Song("Eye of the Tiger","Survivor")
        self.assertEqual("Eye of the Tiger", song_1.song_name)


    def test_song_has_song_name_YMCA(self):
        song_1 = Song("YMCA","Village people")
        self.assertEqual("YMCA",song_1.song_name)

    
    def test_song_has_band_or_artist_name_Survivor(self):
        song_1 = Song("Eye of the Tiger","Survivor")
        self.assertEqual("Survivor", song_1.band_or_artist_name)

    def test_song_has_band_artist_name_Village_People(self):
        song_1 = Song("YMCA","Village People")
        self.assertEqual("Village People",song_1.band_or_artist_name)



