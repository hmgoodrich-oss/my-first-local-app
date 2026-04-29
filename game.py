import random

class Game: 
     def __init__(self):
          self.suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Colonel Mustard", "Mrs. White"]
          self.weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
          self.rooms = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
          self.over = False
          
          self.solution = {}
          self.setup_game()

     def setup_game(self):
          self.solution = {
               "suspect": random.choice(self.suspects),
               "weapon": random.choice(self.weapons),
               "room": random.choice(self.rooms)   
          }
          # test print(self.solution)
    
     def check_accusation(self, args):
          if len(args) < 3:
              print("Accusation should be in the form 'suspect, weapon, room'")
              return
         
          suspect = args[0].strip()
          weapon = args[1].strip()
          room = args[2].strip()
          incorrect = []
          
          if suspect.lower() != self.solution["suspect"].lower():
               incorrect.append(f"suspect: {suspect}")
               print()
          if weapon.lower() != self.solution["weapon"].lower():
               incorrect.append(f"weapon: {weapon}")
          if room.lower() != self.solution["room"].lower():
               incorrect.append(f"room: {room}")
     #give a clue? 
          if incorrect != []:
               print(f"You realize {random.choice(incorrect)} couldn't be it..by jove, it's all coming together!")
          else:
               print("You're on the right track!")

     def make_accusation(self, args):
          if len(args) < 3:
              print("Accusation should be in the form 'suspect, weapon, room'")
          suspect = args[0].strip()
          weapon = args[1].strip()
          room = args[2].strip()
          if suspect.lower() == self.solution["suspect"].lower() and weapon.lower() == self.solution["weapon"].lower() and room.lower() == self.solution["room"].lower():
               print(f"You've done it! Arrest {self.solution['suspect']}")
               self.over = True
               return
          else:
               print(f"You've got the wrong man...it was {self.solution['suspect']} with the {self.solution['weapon']} in the {self.solution['room']}")
               self.over = True
               return
     

     
