import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    # def setUp(self): 
    #     self.room = Room()

    def test_room_has_name_Hello_Kitty(self):
        room_1 = Room("Hello Kitty")
        self.assertEqual("Hello Kitty", room_1.room_name)

    def test_room_has_name_My_Little_Pony(self):
        room_1 = Room("My Little Pony")
        self.assertEqual("My Little Pony", room_1.room_name)