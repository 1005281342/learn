import sys
for line in sys.stdin:

    n = int(line.strip())
    if n <= 1:
        print(1)
    else:
        x = 1
        for i in range(1, n+1):
            x *= i
        str_x = reversed(list(str(x)))
        for char in str_x:
            if char != '0':
                print(char)
                break
