import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.caraoke_bar import CaraokeBar

class TestRoom(unittest.TestCase):

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

    def test_room_has_name_Hello_Kitty(self):
        self.assertEqual("Hello Kitty", self.room_1.room_name)

    def test_room_has_name_My_Little_Pony(self):
        self.assertEqual("My Little Pony", self.room_2.room_name)

    def test_search_for_song_True(self):
        song_request = "Eye of the Tiger"
        self.assertEqual(True, self.room_1.search_for_song(self.caraoke_bar,song_request))

    def test_search_for_song_False(self):
        song_request = "Do They It's Chrimstas Time"
        self.assertEqual(False, self.room_1.search_for_song(self.caraoke_bar,song_request))

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

    def test_play_next_song(self):
        self.room_1.add_song_to_playlist_queue(self.song_1)
        self.room_1.add_song_to_playlist_queue(self.song_2)
        self.guest_1.favourite_song = self.song_1

        self.room_1.play_next_song()
        self.assertEqual(1, self.room_1.count_songs_in_playlist_queue())


