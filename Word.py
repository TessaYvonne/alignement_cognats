class Word:
    def __init__(self, text="", prefix="", letters=None):
        if letters is None:
            letters = []
        self.text = text
        self.letters = letters
        self.prefix = prefix

    def __str__(self):
        '{ text: ' + self.text + ', letters: ' + str(self.letters) + ', prefix: ' + self.prefix + ' }'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

