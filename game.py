import random

import time

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
         if suspect != self.solution["suspect"]:
              incorrect.append("suspect", suspect)
              print()
         if weapon != self.solution["weapon"]:
              incorrect.append("weapon", weapon)
         if room != self.solution["room"]:
              incorrect.append("room", room)
              #give a clue?
     if incorrect:
          print(f"You realize {random.choice(incorrect)} couldn't be it..
               by jove, it's all coming together!")'
     else:
          print("You're on the right track!")
     
     def make_accusation(self, suspect, weapon, room):
         if suspect == self.solution["suspect"] and
               weapon == self.solution["weapon"] and
               room == self.solution["room"]:
               print(f"You've done it! Arrest {self.solution["suspect"]}")
               break
         else:
              print(f"You've got the wrong man...it was {self.solution["suspect"]} with
                    the {self.solution["weapon"]} in the {self.solution["room"]}")
              
 # timer - googled how to do a countdown in python
    start_time = time.time()
    time_limit = 300 
    time_left = time_limit - (time.time() - start_time) #current time - start time
    if time_left = 0:
     print("TIME'S UP! YOU LOSE.")
     break

            