import random

class Game: 
    def __init__(self):
        self.suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Reverend Green", "Colonel Mustard", "Mrs. White"]
        self.weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
        self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
        
        self.solution = {}

        def setup_game(self):
            self.solution = {
                "suspect": random.choice(self.suspects),
                "weapon": random.choice(self.weapons),
                "room": random.choice(self.rooms)   
            }
# end of file