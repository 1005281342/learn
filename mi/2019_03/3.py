import sys

import math

MaxNum = 1 << 28


def p_f(n):
    if n <= 2:
        return 1
    else:
        return p_f(n - 1) + p_f(n - 2)


def isSquare(n):
    sr = int(math.sqrt(n))
    return sr * sr == n


def printPrimeAndFib(n):
    # Using Sieve to generate all
    # primes less than or equal to n.
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:

        # If prime[p] is not changed,
        # then it is a prime
        if prime[p] == True:

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p = p + 1

    return (i for i in range(2, n + 1) if (prime[i] and (isSquare(5 * i * i + 4) > 0 or isSquare(5 * i * i - 4) > 0)))


# res = printPrimeAndFib(MaxNum)
# x = next(res)
# print(x)
for line in sys.stdin:
    line = line.strip()
    n, m = [int(g) for g in line.split(' ')]
    c = 0
    res = printPrimeAndFib(MaxNum)
    while c < n:
        try:
            nn = next(res)
        except:
            pass
        c += 1
    s = (nn//3) % m
    print((9 - len(str(s)))*'*'+str(s))