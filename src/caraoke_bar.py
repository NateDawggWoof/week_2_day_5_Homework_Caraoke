# from src.room import Room
# from src.guest import Guest
# from src.song import Song

class CaraokeBar:
    def __init__(self,caraoke_bar_name):
        self.caraoke_bar_name = caraoke_bar_name

    def check_guest_into_room(self,guest,room):
        room.room_occupants.append(guest)

    def check_guest_out_of_room(self,guest,room):
        room.room_occupants.remove(guest)


