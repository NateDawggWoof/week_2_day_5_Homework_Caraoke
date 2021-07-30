class Room:
    def __init__(self,room_name):
        self.room_name = room_name
        self.room_occupants = []


    def check_number_of_occupants(self):
        return len(self.room_occupants)