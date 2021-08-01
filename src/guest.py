import random

class Guest:
    def __init__(self, name):
        self.guest_name = name
        self.debit_card = random.randint(0,100)



