"""
进程
    os.fork()
    multiprocessing
    启动多个子进程可以使用进程池
    进程间通信
        Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
        Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。


线程
    threading

    多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
    Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
    Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

协程
    yield
    gevent

"""