# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'

    int_line = int(line)

    count = 0
    for x in range(1, int_line + 1):
        if x % 2 == 1:

            count += str(x).count('3')
            # for y in str(x):
            #
            #     if y == '3':
            #         count += 1
    return count


if __name__ == '__main__':

    import time
    start = time.time()
    aa = solution("9999999")
    end = time.time()
    print(aa)
    print(end-start)