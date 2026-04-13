import random

class Game: 
    def __init__(self):
        self.suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Colonel Mustard", "Mrs. White"]
        self.weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
        self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
        
        self.solution = {}
        self.setup_game()

    def setup_game(self):
            self.solution = {
                "suspect": random.choice(self.suspects),
                "weapon": random.choice(self.weapons),
                "room": random.choice(self.rooms)   
            }
    def check_accusation(self, suspect, weapon, room):
         incorrect = []
         if suspect == self.solution["suspect"]:
              incorrect.append("suspect", suspect)
         if weapon == self.solution["weapon"]:
              incorrect.append("weapon", weapon)
         if room == self.solution["room"]:
              incorrect.append("room", room)

            
            