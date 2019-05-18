"""
    File name: stringDatabase.py
    Author: Gursimran Singh
    Python Version: 3.7
    Date Created: 17/05/2019
"""


class StringDatabase:
    """Class to represent a String Database which manages the IO of the Guess Game

    Attributes:
        word (str): The list of words from the file
        _frequencies: The list of frequencies of alphabets
    """
    def __init__(self):
        """StringDatabase init method
        """
        self.word = []
        self._frequencies = {
            "a": "8.17",
            "b": "1.49",
            "c": "2.78",
            "d": "4.25",
            "e": "12.70",
            "f": "2.23",
            "g": "2.02",
            "h": "6.09",
            "i": "6.97",
            "j": "0.15",
            "k": "0.77",
            "l": "4.03",
            "m": "2.41",
            "n": "6.75",
            "o": "7.51",
            "p": "1.93",
            "q": "0.10",
            "r": "5.99",
            "s": "6.33",
            "t": "9.06",
            "u": "2.76",
            "v": "0.98",
            "w": "2.36",
            "x": "0.15",
            "y": "1.97",
            "z": "0.07"
        }

    def load_file(self):
        """StringDatabase load_file method
        """
        self.file = open("four_letters.txt",'r')
        for line in self.file:
            for word in line.strip('\n').split(" "):
                self.word.append(word)
        return self.word


    def get_frequencies(self):
        """StringDatabase get_frequencies method
        """
        return self._frequencies


















