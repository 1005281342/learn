# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    int_10 = int(line)
    int_2 = bin(int_10).replace('0b', '')
    int_2_r = int_2[::-1]
    x = 32 - len(int_2_r)
    int_2_r += '0'*x
    return int(int_2_r, 2)

aa = solution("4626149")
print(aa)
