def tb(x):
    print(x)


async def y(x):
    print(x * 2)


if __name__ == '__main__':
    a = 10
    tb(x=a)
    y(x=a)
