import random

class Guest:
    def __init__(self, name,caraoke_bar):
        self.guest_name = name
        self.debit_card = random.randint(0,100)
        self.max_room_index = caraoke_bar.count_rooms()-1

        self.random_room_index =random.randint(0,self.max_room_index)
        self.preffered_room_choice = caraoke_bar.rooms[self.random_room_index]
        self.responses = ["yes","no"]
        self.only_wants_preffered_room = random.choice(self.responses)
        self.room_allocation = None
        self.favourite_song = random.choice(caraoke_bar.music_librairy)
        self.favourite_song_responses = ["Whoooooo!!!!","Push it to the max!!!","Here we go!!!"]
        self.favourite_song_response = random.choice(self.favourite_song_responses)



