import random

class Dice:
    def __init__(self):
        self.sides = [1, 1, 1, 2, 2, 2, 3, 3, 'X', '+1']
    
    def roll(self):
        return random.choice(self.sides)
