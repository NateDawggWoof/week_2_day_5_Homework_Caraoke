class CaraokeBar:
    def __init__(self,caraoke_bar_name):

        self.caraoke_bar_name = caraoke_bar_name
        self.music_librairy = []

    def check_guest_into_room(self,Guest,Room):
        Room.room_occupants.append(Guest)

    def check_guest_out_of_room(self,guest,Room):
        Room.room_occupants.remove(guest)

    def check_all_guest_out_from_room(self,Room):
        Room.room_occupants.clear()

