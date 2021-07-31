import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room
from src.caraoke_bar import CaraokeBar

class TestCaraokeBar(unittest.TestCase):
    
    def setUp(self):
        self.caraoke_bar = CaraokeBar("Code Clan Caraoke")
        self.room_1 = Room("Hello Kitty")
        self.room_2 = Room("My Little Pony")
        self.caraoke_bar.rooms = [self.room_1, self.room_2]
        self.guest_1 = Guest("Arnold Schwarzenegger")
        self.guest_2 = Guest("Sylvester Stallone")
        self.guest_3 = Guest("Jackie Chan")
        self.guest_4 = Guest("Chris Tucker")

    def test_caraoke_bar_has_name_Code_Clan_Caraoke(self):
        self.assertEqual("Code Clan Caraoke", self.caraoke_bar.caraoke_bar_name)
    
    def test_check_in_guest_into_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.assertEqual(1, self.room_1.check_number_of_occupants())

    def test_check_in_two_guests_into_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_1)
        self.assertEqual(2, self.room_1.check_number_of_occupants())

    def test_check_guests_out_of_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_1)
        self.assertEqual(2, self.room_1.check_number_of_occupants())

        self.caraoke_bar.check_guest_out_of_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_out_of_room(self.guest_2,self.room_1)
        self.assertEqual(0, self.room_1.check_number_of_occupants())

    def test_check_all_guests_out_from_room(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_3,self.room_2)
        self.caraoke_bar.check_guest_into_room(self.guest_4,self.room_2)
        self.assertEqual(2, self.room_1.check_number_of_occupants())
        self.assertEqual(2, self.room_2.check_number_of_occupants())

        self.caraoke_bar.check_all_guests_out_from_room(self.room_1)
        self.assertEqual(0, self.room_1.check_number_of_occupants())
        self.assertEqual(2, self.room_2.check_number_of_occupants())

    def test_check_all_guests_out_from_all_rooms(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.caraoke_bar.rooms[0])
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.caraoke_bar.rooms[0])
        self.caraoke_bar.check_guest_into_room(self.guest_3,self.caraoke_bar.rooms[1])
        self.caraoke_bar.check_guest_into_room(self.guest_4,self.caraoke_bar.rooms[1])
        room_1 = self.caraoke_bar.rooms[0]
        room_2 = self.caraoke_bar.rooms[1]
        self.assertEqual(2, room_1.check_number_of_occupants())
        self.assertEqual(2, room_2.check_number_of_occupants())

        self.caraoke_bar.check_all_guests_out_from_all_rooms()
        self.assertEqual(0, room_1.check_number_of_occupants())
        self.assertEqual(0, room_2.check_number_of_occupants()) 

    def test_add_room(self):
        self.caraoke_bar.add_room()
        self.assertEqual(3,self.caraoke_bar.count_rooms())
        
    def test_room_names(self):
        self.assertEqual(['Hello Kitty', 'My Little Pony'], self.caraoke_bar.print_room_names())

    def test_remove_room(self):
        self.caraoke_bar.remove_room("Hello Kitty")
        self.assertEqual(1,self.caraoke_bar.count_rooms())