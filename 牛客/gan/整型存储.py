import sys

strings = sys.stdin.readline().strip()[:10]

str_list = strings.split(' ')

for st in str_list:

    if st and int(st):
        print(int(st), int(''.join(reversed(st))))
