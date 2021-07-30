import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    # def setUp(self):

    def test_song_has_name_Eye_Of_The_Tiger(self):
        song_1 = Song("Eye of the Tiger","Survivor")
        self.assertEqual("Eye of the Tiger", song_1.song_name)
