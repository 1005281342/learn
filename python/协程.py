"""
廖雪峰的官方网站
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432090171191d05dae6e129940518d1d6cf6eeaaa969000
和多线程比，协程有何优势？

    最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
    因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

    第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，
    只需要判断状态就好了，所以执行效率比多线程高很多。

    因为协程是一个线程执行，那怎么利用多核CPU呢？
    最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

    多线程死锁如何解决
        改用协程！！

        传统的生产者-消费者模型是一个线程写消息，一个线程取消息，
            通过锁机制控制队列和等待，但一不小心就可能死锁。

        如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，
            待消费者执行完毕后，切换回生产者继续生产，效率极高。
"""

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

    # 消费者
    def consumer():
        r = ''
        while True:
            n = yield r
            if not n:
                return
            print('[CONSUMER] Consuming %s...' % n)
            r = '200 OK'

    # 生产者
    def produce(c):     # 接受一个生成器对象
        c.send(None)
        n = 0
        while n < 5:
            n = n + 1
            print('[PRODUCER] Producing %s...' % n)
            r = c.send(n)
            print('[PRODUCER] Consumer return: %s' % r)
        c.close()

    c = consumer()  # 实例化消费者生成器对象
    produce(c)

"""
    如何知道是谁产出 "6" 结束程序
        -- 看 send 6
"""