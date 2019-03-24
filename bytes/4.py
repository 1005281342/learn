import sys

a, b = sys.stdin.readline().strip().split(' ')

c = sys.stdin.readline().strip()

a_list = []
b_list = []
for i, char in enumerate(c):

    if char == 'a':
        a_list.append(i)
    else:
        b_list.append(i)

b_bak = []
if len(a_list) > len(b_list):
    for x in range(len(b_list)-2):
        b_bak.append(b_list[x+2])
