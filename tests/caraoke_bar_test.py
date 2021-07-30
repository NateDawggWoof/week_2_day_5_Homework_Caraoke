import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room
from src.caraoke_bar import CaraokeBar

class TestCaraokeBar(unittest.TestCase):
    
    def setUp(self):
        self.caraoke_bar = CaraokeBar("Code Clan Caraoke")

    def test_caraoke_bar_has_song_name_Code_Clan_Caraoke(self):
        self.assertEqual("Code Clan Caraoke", self.caraoke_bar.caraoke_bar_name)

