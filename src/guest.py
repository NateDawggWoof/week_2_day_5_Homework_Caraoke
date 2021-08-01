import random

class Guest:
    def __init__(self, name,caraoke_bar):
        self.guest_name = name
        self.debit_card = random.randint(0,100)
        self.preffered_room_choice = random.choice(caraoke_bar.rooms)
        self.only_wants_preffered_room = random.choice(yes, no)



