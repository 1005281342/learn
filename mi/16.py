import sys

for line in sys.stdin:
    line = line.strip()
    try:
        print(round(eval(line)))
    except:
        print('err')
