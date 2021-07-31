from src.song import Song
from src.room import Room

class CaraokeBar:
    def __init__(self,caraoke_bar_name):

        self.caraoke_bar_name = caraoke_bar_name
        self.rooms =[]
        self.music_librairy = []

    def check_guest_into_room(self,Guest,Room):
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
        for room in self.rooms:
            self.rooms.remove(room)

    def add_song_to_music_libriary(self):
        Song_x =  Song(input("Please enter song name :"), input("Please enter Band or Artist name :"))
        self.music_librairy.append(Song_x)

    def count_songs_in_music_librairy(self):
        return len(self.music_librairy)

    