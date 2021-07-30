import unittest
from src.room import Room
from src.song import Song
from src.caraoke_bar import CaraokeBar

class TestRoom(unittest.TestCase):

    def setUp(self): 
        self.caraoke_bar_1 = CaraokeBar("Code Clan Caraoke")
        self.room_1 = Room("Hello Kitty")
        self.room_2 = Room("My Little Pony")
        self.song_1 = Song("Eye Of The Tiger","Survivor")
        self.song_2 = Song("YMCA","Village People")
        self.caraoke_bar_1.music_librairy = [self.song_1,self.song_2]


    def test_room_has_name_Hello_Kitty(self):
        self.assertEqual("Hello Kitty", self.room_1.room_name)

    def test_room_has_name_My_Little_Pony(self):
        self.assertEqual("My Little Pony", self.room_2.room_name)

    def test_search_for_song_True(self):
        song_request = "eye of the tiger"
        self.assertEqual(True, self.room_1.search_for_song(self.caraoke_bar_1,song_request))

    def test_search_for_song_False(self):
        song_request = "Do They It's Chrimstas Time"
        self.assertEqual(False, self.room_1.search_for_song(self.caraoke_bar_1,song_request))

    def test_add_song_to_playlist_queue(self):
        self.room_1.add_song_to_playlist_queue(self.song_1)
        self.room_1.add_song_to_playlist_queue(self.song_2)
        self.assertEqual(2, self.room_1.count_songs_in_playlist_queue())

    def test_remove_song_to_playlist_queue(self):
        self.room_1.add_song_to_playlist_queue(self.song_1)
        self.room_1.add_song_to_playlist_queue(self.song_2)
        self.assertEqual(2, self.room_1.count_songs_in_playlist_queue())

        self.room_1.remove_song_from_playlist_queue(self.song_1)
        self.assertEqual(1, self.room_1.count_songs_in_playlist_queue())


