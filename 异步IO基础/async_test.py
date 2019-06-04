#

import asyncio


# 给函数添加异步属性
async def add_async_func(func, user):
    func(user)
    await asyncio.sleep(0.2)


def print_hello(user):
    print('hello', user)
    with open('test') as f:
        f.write(str(user))


if __name__ == '__main__':
    asyncio.ensure_future(add_async_func(func=print_hello, user=123))
