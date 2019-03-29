import sys

for line in sys.stdin:
    line = line.strip()
    try:
        print(int(eval(line)))
    except:
        print('err')