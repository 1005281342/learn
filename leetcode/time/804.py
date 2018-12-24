class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        mapping_map = {
            'a': ".-",
            'b': "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--..",
        }

        a_set = {'', }
        for word in words:

            tmp_string = ''
            for char in word:
                tmp_string += mapping_map[char]
            a_set.add(tmp_string)

        return len(a_set) - 1
