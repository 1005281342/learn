for x in range(16):
    if str(x*x) == ''.join(reversed(str(x*x))):
        print(x*x)
