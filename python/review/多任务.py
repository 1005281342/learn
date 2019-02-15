import os
# from time import sleep

pid = os.fork()

# 多进程中所有数据各自拥有一份，互不干扰
num = 0
if pid == 0:
    num += 1
    print(num, " do 1")
else:
    num += 1
    # sleep(1)
    print(num, " do 2")

# 多次fork()
pid = os.fork()
if pid == 0:
    num += 1
    print(num, " do 3")
else:
    num += 1
    # sleep(1)
    print(num, " do 4")

# 父子进程执行顺序没有规律， 完全取决于操作系统的调度算法
