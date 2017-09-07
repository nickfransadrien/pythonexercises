from random import choice

words = ["chair","church","television","game","television","scientist"]

class Game:
    def __init__(self):
        self.word = choice(words)
        self.letters = set(self.word)
        self.guessed_letters = []
    def guess(self,letter):
        if letter in self.letters:
            if letter not in self.guessed_letters:
                self.guessed_letters += letter

    def guessed_word(self):
        return len(self.guessed_letters) == len(self.letters)
        
    def print_word(self):
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter,end="")
            else:
                print("_",end="")
            print(" ",end="")
        print("")

game = Game()

def get_letter():
    while True:
        letter = input("Guess a letter:")
        if letter.isalpha() and len(letter) == 1:
            return letter.lower()
        print("That's not a letter.")    

while True:
    game.print_word()
    if game.guessed_word():
        print("You guessed it!")
        break
    letter = get_letter()
    game.guess(letter)





    



            




