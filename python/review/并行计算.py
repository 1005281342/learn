from time import sleep
import concurrent.futures


def test(iterable_range):
    for _ in iterable_range:
        sleep(1)


def write_text(iterable_range):
    with open('a_test.txt', 'w') as f:
        for i in iterable_range:
            f.write(str(i))


def create_text(iterable_range):
    for i in iterable_range:
        with open('test_' + str(i) + '.txt', 'w') as _:
            # f.write('')
            pass


# create_text(range(1, 10))

for x in [range(1, 10)]*16:
    test(x)     # sleep 10 * 16

# 使用并行
with concurrent.futures.ProcessPoolExecutor() as ex:
    res = ex.map(test, [range(1, 10)]*16)

    # 但是在 python3中，返回是一个迭代器，所以它其实是不可调用的 <class 'generator'>
    print(type(res))
    res.__next__()      # sleep 10*16/os.cpu_count()
