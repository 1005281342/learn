class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """

        length = len(letter)
        for w in self.words:
            if len(w) > length:
                if w.find(letter) > 0:
                    return True
            elif w == letter:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
words = ["cd", "f", "kl"]
letter = 'de'
obj = StreamChecker(words)
param_1 = obj.query(letter)
print(param_1)
