import random
"""
    这是一段simple_coroutine协程和main交互切换执行的过程演示，
    simple_coroutine协程和main只要有一方随机产出6则终止执行，
    否则就会一直切换执行
"""


# 带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator
def simple_coroutine():
    print('coroutine started')
    while True:
        send = random.choice(range(10))
        print('coroutine send', send)
        if send == 6:
            yield send
            break

        receive = yield send
        print('coroutine receive', receive)


if __name__ == '__main__':

    """
        GEN_CREATE:创建，等待开始执行
        GEN_RUNNING:生成器执行中
        GEN_SUSPENDED:在yield表达式处暂停
        GEN_CLOSE:执行结束，生成器关闭
    """

    from inspect import getgeneratorstate

    print('main started')
    coroutine = simple_coroutine()
    print('main declare', coroutine)
    print("*", getgeneratorstate(coroutine))
    receive = next(coroutine)
    print('main next', receive)
    while receive != 6:
        send = random.choice(range(8))
        print('main send', send)
        if send == 6:
            coroutine.send(send)
            print("**", getgeneratorstate(coroutine))
            coroutine.close()
            print("***", getgeneratorstate(coroutine))
            break
        receive = coroutine.send(send)
        print("****", getgeneratorstate(coroutine))
        print('main receive', receive)


# if __name__ == '__main__':
#     print('main started')
#     coroutine = simple_coroutine()  # 实例化一个生成器， 得到一个对象
#     print('main declare', coroutine)
#     receive = next(coroutine)   # 先调用
#     # receive = coroutine.__next__()   # 先调用
#     print('main next', receive)
#     while receive != 6:
#         send = random.choice(range(8))
#         print('main send', send)
#
#         # main 产出了6，通知 simple_coroutine， 并关闭
#         if send == 6:
#             coroutine.send(send)
#             coroutine.close()
#             break
#         receive = coroutine.send(send)  # 让步给协程
#         print('main receive', receive)


"""
    如何知道是谁产出 "6" 结束程序
        -- 看 send 6

"""