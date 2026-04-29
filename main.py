from game import Game
game = Game()
# gameplay
tries = 0
print("It's a dark and stormy night...and your dinner party has just been interrupted by a murder! It's up to you to find out who, how, and where.")
print(f"It must be one of these people: {game.suspects} with one of these objects: {game.weapons} in one of these rooms: {game.rooms}")
while tries <= 10 and game.over == False:
    print("\n")
    print("1. Make an accusation")
    print("2. Make an arrest")
    print("3. Check Notes")
    print("4. Give up :(")
    print("\n")
    choice = input("Let's:")
    if choice == "1":
        ans = input("Who did it? With what? and Where?")
        args = ans.split(',')
        # print(f'args: {args}')
        game.check_accusation(args)
    elif choice == "2":
        ans = input("Who did it? With what? and Where?")
        args = ans.split(',')
        game.make_accusation(args)
    elif choice == "3":
        game.display_evidence()
    elif choice == "4":
        break
    else:
        print("You're talking nonsense, detective...what should we do?")