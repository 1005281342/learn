from time import sleep
import concurrent.futures


def test(iterable_range):
    for _ in iterable_range:
        sleep(1)


# 使用并行
with concurrent.futures.ProcessPoolExecutor() as ex:
    ex.map(test, range(1, 10))
