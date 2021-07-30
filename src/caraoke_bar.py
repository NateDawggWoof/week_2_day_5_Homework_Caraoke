class CaraokeBar:
    def __init__(self,caraoke_bar_name):

        self.caraoke_bar_name = caraoke_bar_name
        self.music_librairy = []

    def check_guest_into_room(self,guest,room):
        room.room_occupants.append(guest)

    def check_guest_out_of_room(self,guest,room):
        room.room_occupants.remove(guest)


