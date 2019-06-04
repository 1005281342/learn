import asyncio


async def foo():
    print("这是一个协程")


async def foo_2():
    print("这也是一个协程")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 定义一个事件循环
    try:
        print("开始运行协程")
        print("进入事件循环")
        loop.run_until_complete(foo())  # 运行协程
        loop.run_until_complete(foo_2())  # 运行协程

    finally:
        print("关闭事件循环")
        loop.close()  # 运行完关闭协程
