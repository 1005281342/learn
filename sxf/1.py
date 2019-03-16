import sys

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    # print(s)

    s = s.lower()

    d = dict()
    for char in s:
        if char not in {'b', 'n', 't', 'w', 'z', 'j', 'e', 's', 'y', 'x', 'm', 'i', 'r', 'g', 'v', 'o', 'q', 'a', 'l',
                        'k', 'f', 'u', 'p', 'd', 'c', 'h'}:
            continue
        if d.get(char):
            d[char] += 1
            if d[char] == 3:
                print(ord(char) - 96)
                break
        else:
            d[char] = 1
