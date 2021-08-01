from src.song import Song
from src.room import Room
from src.guest import Guest

class CaraokeBar:
    def __init__(self,caraoke_bar_name):

        self.caraoke_bar_name = caraoke_bar_name
        self.rooms =[]
        self.music_librairy = []

    def guest_details():
        Guest_X = Guest(input("Enter guest full name"))
        return Guest_X
         

    def check_guest_into_room(self,Guest=None,Room=None):
        if Guest == "test":
            Guest = self.guest_details()
            Room.room_occupants.append(Guest)
        else:
            Room.room_occupants.append(Guest)

    def check_guest_out_of_room(self,guest,Room):
        Room.room_occupants.remove(guest)

    def check_all_guests_out_from_room(self,Room):
        Room.room_occupants.clear()

    def check_all_guests_out_from_all_rooms(self):
        for Room in self.rooms:
            Room.room_occupants.clear()

    def add_room(self):
        Room_x =  Room(input("Please enter room name :"))
        self.rooms.append(Room_x)

    def count_rooms(self):
        return len(self.rooms)

    def print_room_names(self):
        room_names = [room.room_name for room in self.rooms]
        print(list(room_names))
        return room_names

    def remove_room(self,room_name):
        for Room in self.rooms:
            if Room.room_name == room_name:
                self.rooms.remove(Room)

    def add_song_to_music_libriary(self):
        Song_x =  Song(input("Please enter song name :"), input("Please enter Band or Artist name :"))
        self.music_librairy.append(Song_x)

    def count_songs_in_music_librairy(self):
        return len(self.music_librairy)

    
    def remove_song_from_music_libriary(self,song_name):
        for Song in self.music_librairy:
            if Song.song_name == song_name:
                self.music_librairy.remove(Song)

    def print_music_libriary(self):
        libriary_list = [Song.song_name + " by " + Song.band_or_artist_name for Song in self.music_librairy]
        print(list(libriary_list))
        return libriary_list
    