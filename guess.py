import sys
import random


from game import Game
from stringDatabase import StringDatabase


class Guess():
    def __init__(self):
        self.words_list = StringDatabase().load_file()
        self.random_word = "random"
        self.game_Obj = []
        self.tuple_word = ['-', '-', '-', '-']
        self.bad_guesses = 0
        self.missed_letters = 0
        self.game_count = 1
        self.status = None
        self.end_game = False


    def get_random_word(self):
        self.random_word = random.choice(self.words_list)
        print(self.random_word)

    def set_tuple_letter(self, index, letter):
        self.tuple_word[index] = letter
        temp_word = ''
        for w in self.tuple_word:
            temp_word += w

        if temp_word == self.random_word:
            self.status = 'Success'

    def print_tuple_current_guess(self):
        print("Current Guess: ", self.tuple_word)

    def print_menu(self):
        self.get_random_word()

        loop = 1
        while loop == 1:
            if self.status:
                self.end_game

            print("***** The great guessing game *****\n\n")
            self.print_tuple_current_guess()
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
        if guessed_word == self.random_word:
            print("You Guessed it!")
            print('The word is: "{}"!\n'.format(self.random_word))
            self.status = 'Success'
        else:
            print("Wrong! Sorry try again!")
            self.bad_guesses += 1

    def guess_letter(self):
        letter = input('\n\nEnter a letter.')
        indexes = [index for index, element in enumerate(self.random_word) if element == letter]
        #print(indexes)
        if letter in self.random_word:
            print("You found {} letter(s)! : ".format(len(indexes)))
            if len(indexes) > 1:
                for i in indexes:
                    self.set_tuple_letter(i, letter)
            else:
                self.set_tuple_letter(self.random_word.find(letter), letter)

        else:
            print("Sorry no such letter found!")
            self.missed_letters += 1


    def create_new_game_obj(self):
        self.game_Obj.append(Game())




if __name__ == '__main__':

    guess_game = Guess()
    guess_game.print_menu()