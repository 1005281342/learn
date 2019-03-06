import sys

m = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'E',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'I',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'O',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'U',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
    'z': 'A',
}

for line in sys.stdin:
    # a = line.split()
    # print(line)
    s = ''
    for char in line:
        if m.get(char):
            s += m[char]
        else:
            s += char
    print(s)
