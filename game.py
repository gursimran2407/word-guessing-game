"""
    File name: game.py
    Author: Gursimran Singh
    Python Version: 3.7
    Date Created: 17/05/2019
"""


class Game:
    """Class Game to store a game data.

    Attributes:
        _word (str): The random word for each game
        _game: The number of game
        _status: The status of the gam
        _bad_guesses: The number of bad guesses
        _missed_letters: The number of missed letters
        _score: The final score of the game
    """
    def __init__(self):
        """Game init method """
        self._game = 1
        self._word = None
        self._status = None
        self._bad_guesses = 0
        self._missed_letters = 0
        self._score = 0

    @property
    def game_number(self):
        """Getter for game_number"""
        return self._game

    @game_number.setter
    def game_number(self, number):
        """Setter for game_number"""
        self._game = number

    @property
    def words(self):
        """Getter for word"""
        return self._word

    @words.setter
    def words(self, word):
        """Setter for the word"""
        self._word = word

    @property
    def statuss(self):
        """Getter for the status"""
        return self._status

    @statuss.setter
    def statuss(self, status):
        """Setter for the status of the game"""
        self._status = status

    @property
    def bad_guesses(self):
        """Getter for the number of bad guesses"""
        return self._bad_guesses

    @bad_guesses.setter
    def bad_guesses(self, bad_guess):
        """Setter for the number of bad guesses"""
        self._bad_guesses = bad_guess

    @property
    def missed_letterss(self):
        "Getter for the number of missed letters"
        return self._missed_letters

    @missed_letterss.setter
    def missed_letterss(self, missed_letters):
        "Setter for the number of missed letters"
        self._missed_letters = missed_letters

    @property
    def scores(self):
        """Getter for the scores"""
        return self._score

    @scores.setter
    def scores(self, score):
        """Setter for the scores"""
        self._score = score

    def __str__(self):
        """To string function to convert object to the string"""

        string = '  '+str(self._game) + '\t\t'+\
                 self._word+'\t\t'+self._status+'\t\t\t\t'+str(self._bad_guesses) \
                 + '\t\t\t  ' + str(self._missed_letters)+'\t\t\t  ' + str(self._score)

        return string









