class StringDatabase:
    def __init__(self):
        self.word = []

    def load_file(self):
        self.file = open("four_letters.txt",'r')
        for line in self.file:
            for word in line.strip('\n').split(" "):
                self.word.append(word)
                #print(word)

        return self.word

















