class Player_notes:
    def __init__(self): 
        self.guesses = []
    def add_guess(self, guess):
        self.guesses.append(guess)
        # test print("guesses length:",len(self.guesses))
    def display_guesses(self):
        for i in range(0,len(self.guesses)):
            print(f"{i}. Guess: {self.guesses[i].suspect}, {self.guesses[i].weapon}, {self.guesses[i].room} Exonerated: {self.guesses[i].response}")