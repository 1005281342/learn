import os
import psutil


def system_rate():
    """ 内存与CPU使用率 """
    # 获取当前运行的pid
    p1 = psutil.Process(os.getpid())

    # 本机内存的占用率
    print('内存占用率： ' + str(psutil.virtual_memory().percent) + '%')

    # 本机cpu的总占用率
    print('CPU_0占用率： ' + str(psutil.cpu_percent(0)) + '%')
    print('CPU_1占用率： ' + str(psutil.cpu_percent(1)) + '%')
    print('CPU_2占用率： ' + str(psutil.cpu_percent(2)) + '%')
    print('CPU_3占用率： ' + str(psutil.cpu_percent(3)) + '%')

    # # 该进程所占cpu的使用率
    # print("该进程CPU占用率: " + str(p1.cpu_percent(None)) + "%")

    # 该进程所占内存占用率
    print("该进程内存占用率: " + str(p1.memory_percent()) + "%")


if __name__ == '__main__':
    system_rate()
