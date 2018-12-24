"""
输入

    输入3个数，以空格分隔： 第1个数是待转换的数， 第2个数是待转换的数的进制， 第3个数是转换后的数的进制。

输出

    输入转换后的数

输入样例

    31 10 16

输出样例

    1f

"""

# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    num, frist_type, last_type = line.strip().split(' ')

    # 转为10进制
    num_10 = int(num, int(frist_type))

    last_type = int(last_type)

    # 转为其他进制
    def f(n, x):

        # n为待转换的十进制数，x为机制，取值为2-16
        a = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        b = []
        while True:
            s = n//x    # 商
            y = n % x   # 余数
            b.append(int(y))
            if s == 0:
                break
            n = s

        ss = ''
        while b:
            ss += a[b.pop()]

        return ss

    return f(num_10, last_type)


aa = solution('31 10 16')
print(aa)
