import sys

for line in sys.stdin:
    line = line.strip()
    a, b = [int(x) for x in line.split(' ')]
    big_num = '0x' + ''.join([hex(x).replace('0x', '') for x in range(a, b + 1)])
    print(int(big_num, 16) % 15)
