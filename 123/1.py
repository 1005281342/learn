import sys


def FizzBuzz(num):
    for i in range(1, int(num) + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))


for line in sys.stdin:
    a = line.split()
    FizzBuzz(num=a[0])
