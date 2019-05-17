class Game:
    def __init__(self):
        self._game = 1
        self._word = None
        self._status = None
        self._bad_guesses = 0
        self._missed_letters = 0
        self._score = 0

    @property
    def game_number(self):
        return self._game

    @game_number.setter
    def game_number(self, number):
        self._game = number

    @property
    def words(self):
        return self._word

    @words.setter
    def words(self, word):
        self._word = word

    @property
    def statuss(self):
        return self._status

    @statuss.setter
    def statuss(self, status):
        self._status = status

    @property
    def bad_guesses(self):
        return self._bad_guesses

    @bad_guesses.setter
    def bad_guesses(self, bad_guess):
        self._bad_guesses = bad_guess

    @property
    def missed_letterss(self):
        return self._missed_letters

    @missed_letterss.setter
    def missed_letterss(self, missed_letters):
        self._missed_letters = missed_letters

    @property
    def scores(self):
        return self._score

    @scores.setter
    def scores(self, score):
        self._score = score

    def __str__(self):
        # string = 'GameObject(game_number: '+str(self._game) + \
        #          ' ,word ='+self._word+' ,status ='+self._status+' ,bad_guesses ='+str(self._bad_guesses)\
        #          +' ,missed_letters ='+str(self._missed_letters)+' ,score ='+str(self._score)\
        #          + ')'

        string = '  '+str(self._game) + '\t\t'+\
                 self._word+'\t\t'+self._status+'\t\t\t\t'+str(self._bad_guesses) \
                 + '\t\t\t  ' + str(self._missed_letters)+'\t\t\t\t' + str(self._score)

        return string









