def total(a=5, *args, **kwargs):

    """

    :param a:
    :param args:
    :param kwargs:
    :return:
    """

    print(a)

    for x in args:

        print(x)

    for c, d in kwargs.items():
        print(c, d)


print(total(100, 1, 2, 3, Jack=1234, aa=4321))
print(total.__doc__)

a = [1, 2, 3, 4]
del a[0]
