import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room
from src.caraoke_bar import CaraokeBar

class TestCaraokeBar(unittest.TestCase):
    
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

    def test_add_song_to_music_libriary(self):
        self.caraoke_bar.add_song_to_music_libriary()
        self.assertEqual(3,self.caraoke_bar.count_songs_in_music_librairy())

    def test_remove_song_from_music_libriary(self):
        self.caraoke_bar.remove_song_from_music_libriary("YMCA")
        self.assertEqual(1,self.caraoke_bar.count_songs_in_music_librairy())

    def test_print_music_libriary(self):
        self.assertEqual(['YMCA by The Village People', 'Eye of the Tiger by Survivor'], self.caraoke_bar.print_music_libriary())

    def test_check_space_availability_0_spaces(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_1)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_1)
        self.assertEqual(0,self.room_1.check_space_availability())

    def test_check_space_availability_3_spaces(self):
        self.caraoke_bar.check_guest_into_room(self.guest_1,self.room_2)
        self.caraoke_bar.check_guest_into_room(self.guest_2,self.room_2)
        self.assertEqual(3,self.room_2.check_space_availability())

    def test_funds_check_transaction_validity_False(self):
        self.guest_1.debit_card = 0
        self.assertEqual(False,self.caraoke_bar.funds_check_transaction_validity(self.guest_1, self.caraoke_bar.session_price_30mins))

    def test_funds_check_transaction_validity_True(self):
        self.guest_1.debit_card = 100
        self.assertEqual(True,self.caraoke_bar.funds_check_transaction_validity(self.guest_1, self.caraoke_bar.session_price_30mins))

    def test_funds_add_to_balance(self):
        self.guest_1.debit_card = 50
        self.caraoke_bar.funds_add_to_balance(self.guest_1,self.caraoke_bar.session_price_60mins)
        self.assertEqual(108,self.caraoke_bar.balance)
        self.assertEqual(42,self.guest_1.debit_card)

    def test_funds_refund_from_balance(self):
        self.guest_1.debit_card = 50
        self.caraoke_bar.funds_refund_to_guest(self.guest_1,self.caraoke_bar.session_price_30mins)
        self.assertEqual(95,self.caraoke_bar.balance)
        self.assertEqual(55,self.guest_1.debit_card)