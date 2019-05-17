import sys
import random


from game import Game
from stringDatabase import StringDatabase


class Guess():
    def __init__(self):
        self.words_list = StringDatabase().load_file()
        self.random_word = self.get_random_word()
        self.game_Obj = []
        self.bad_guesses = 0
        self.missed_letters = 0


    def get_random_word(self):
        self.random_word = random.choice(self.words_list)
        print(self.random_word)
        return self.random_word

    def print_current_guess(self, one, two, three, four):
        tuple_word = (one, two, three, four)
        print("Current Guess: {}{}{}{}".format(tuple_word[0], tuple_word[1], tuple_word[2], tuple_word[3]))


    def print_menu(self):
        loop = 1
        while loop == 1:

            print("***** The great guessing game *****\n\n")
            self.print_current_guess('-', '-', '-', '-')
            print("\n\ng = guess, t = tell me, l for a letter, and q to quit\n")
            ans = input("Please select a choice.")

            if ans == 'l':
                self.guess_letter()

            elif ans == 'g':
                self.guess_word()

            elif ans == 't':
               print('The word is: "{}"\n'.format(self.random_word))

            elif ans == 'q':
                sys.exit()

    def guess_word(self):
        print("""** The great guessing game **\n\n""")
        guessed_word = input('Enter the whole word.')
        if guessed_word==self.random_word:
            print("You Guessed it!")
            print('The word is: "{}"!\nWant to Play Again?'.format(self.random_word))
        else:
            print("Wrong! Sorry try again!")

    def guess_letter(self):
        letter = input('Enter a letter.')
        if letter in self.random_word:
            print("You found 1 letter! at position: {}".format(self.random_word.index(letter)))

        if letter not in self.random_word:
            print("Sorry no such letter found!")
            if self.missed_letters > 0:
                self.missed_letters += 1


    def create_new_game_obj(self):
        self.game_Obj.append(Game())











if __name__ == '__main__':

    guess_game = Guess()
    guess_game.print_menu()