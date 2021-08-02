from src.song import Song
from src.room import Room
from src.guest import Guest

class CaraokeBar:
    def __init__(self,caraoke_bar_name,balance=0):

        self.caraoke_bar_name = caraoke_bar_name
        self.balance = balance
        self.rooms =[]
        self.music_librairy = []
        self.session_price_30mins = 5
        self.session_price_60mins = 8

    def guest_details():
        guest_X = guest(input("Enter guest full name"))
        return guest_X
         

    def check_guest_into_room(self,guest=None,room=None):
        if guest == "test":
            guest = self.guest_details()
            room.room_occupants.append(guest)
        else:
            room.room_occupants.append(guest)

    def check_guest_out_of_room(self,guest,room):
        room.room_occupants.remove(guest)

    def check_all_guests_out_from_room(self,room):
        room.room_occupants.clear()

    def check_all_guests_out_from_all_rooms(self):
        for room in self.rooms:
            room.room_occupants.clear()

    def add_room(self):
        room_x =  Room(input("Please enter room name :"))
        self.rooms.append(room_x)

    def count_rooms(self):
        return len(self.rooms)

    def print_room_names(self):
        room_names = [room.room_name for room in self.rooms]
        print(list(room_names))
        return room_names

    def remove_room(self,room_name):
        for room in self.rooms:
            if room.room_name == room_name:
                self.rooms.remove(room)

    def add_song_to_music_libriary(self):
        song_x = Song(input("Please enter song name :"), input("Please enter Band or Artist name :"))
        self.music_librairy.append(song_x)

    def count_songs_in_music_librairy(self):
        return len(self.music_librairy)

    
    def remove_song_from_music_libriary(self,song_name):
        for song in self.music_librairy:
            if song.song_name == song_name:
                self.music_librairy.remove(song)

    def print_music_libriary(self):
        libriary_list = [song.song_name + " by " + song.band_or_artist_name for song in self.music_librairy]
        print(list(libriary_list))
        return libriary_list

    def funds_check_transaction_validity(sefl,guest, purchase):
        if guest.debit_card >= purchase:
            return True
        else:
            return False

    def funds_add_to_balance(self, guest, purchase):
        self.balance += purchase
        guest.debit_card -= purchase

    def funds_refund_to_guest(self, guest, purchase):
        self.balance -= purchase
        guest.debit_card += purchase

    