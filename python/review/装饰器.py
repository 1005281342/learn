def say_hello(func):

    def Q():
        func()
        print("hello")

    return Q


@say_hello
def xa():
    print(123)
    return


if __name__ == '__main__':
    a = xa()
