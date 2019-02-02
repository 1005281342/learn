from time import sleep
import threading

s = 0

ss = [100, 200, 300, 400]


def doubler(number):
    """
    可以被线程使用的一个函数
    """
    global s
    while True:
        if ss:
            print("**", ss.pop())
        print(s)
        s += 20

        sleep((1000-s)/100)
        if s > 400:
            break

    print(threading.currentThread().getName() + '\n')
    # print(number * 2)
    # print()


if __name__ == '__main__':

    # while s < 220:
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
        # print("s", s)

