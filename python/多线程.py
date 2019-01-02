import threading

s = 0


def doubler(number):
    """
    可以被线程使用的一个函数
    """
    global s
    s += 20
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()


if __name__ == '__main__':

    while s < 220:
        for i in range(5):
            my_thread = threading.Thread(target=doubler, args=(i,))
            my_thread.start()

        print("s", s)