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
          # murderer = random.choice(self.suspects)
          # mweapon = random.choice(self.weapons)
          # scene = random.choice(self.rooms)
          # self.solution = {murderer, mweapon, scene}
          self.solution = {
               "suspect": random.choice(self.suspects),
               "weapon": random.choice(self.weapons),
               "room": random.choice(self.rooms)   
          }
          print(self.solution)
    
     def check_accusation(self, args):
          if len(args) < 3:
              print("Accusation should be in the form 'suspect, weapon, room'")
          suspect = args[0]
          weapon = args[1]
          room = args[2]
          incorrect = []
          # if suspect != murderer:
          #      incorrect.append(f"suspect: {suspect}")
          #      print()
          # if weapon != mweapon:
          #      incorrect.append(f"weapon: {weapon}")
          # if room != scene:
          #      incorrect.append(f"room: {room}")
          if suspect != self.solution["suspect"]:
               incorrect.append(f"suspect: {suspect}")
               print()
          if weapon != self.solution["weapon"]:
               incorrect.append(f"weapon: {weapon}")
          if room != self.solution["room"]:
               incorrect.append(f"room: {room}")
     #give a clue? 
          if incorrect != []:
               print(f"You realize {random.choice(incorrect)} couldn't be it..by jove, it's all coming together!")
          else:
               print("You're on the right track!")

     def make_accusation(self, args):
          if len(args) < 3:
              print("Accusation should be in the form 'suspect, weapon, room'")
          suspect = args[0]
          weapon = args[1]
          room = args[2]
          if suspect == self.solution["suspect"] and weapon == self.solution["weapon"] and room == self.solution["room"]:
               print(f"You've done it! Arrest {self.solution['suspect']}")
               break
          else:
               print(f"You've got the wrong man...it was {self.solution['suspect']} with the {self.solution['weapon']} in the {self.solution['room']}")
               break
     
game = Game()
# gameplay
tries = 0
print("It's a dark and stormy night...and your dinner party has just been interrupted by a murder! It's up to you to find out who, how, and where.")
print(f"It must be one of these people: {game.suspects} with one of these objects: {game.weapons} in one of these rooms: {game.rooms}")
while tries <= 10:
     print("1. Make an accusation")
     print("2. Make an arrest")
     choice = int(input("Let's:"))
     if choice == 1:
          ans = input("Who did it? With what? and Where?")
          args = ans.split(',')
          # print(f'args: {args}')
          game.check_accusation(args)
     if choice == 2:
          ans = input("Who did it? With what? and Where?")
          args = ans.split(',')
          game.make_accusation(args)
