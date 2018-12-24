# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    a, b, ab = line.strip().split(',')
    a_list = [x for x in a]
    b_list = [x for x in b]
    n = 0
    for char in ab:

        if n % 2 == 0 and a_list and char == a_list[0]:
            a_list.remove(char)
        elif b_list and char == b_list[0]:
            b_list.remove(char)
            n = 1
        elif n % 2 == 1 and a_list and char == a_list[0]:
            a_list.remove(char)
            n = 0
        else:
            return 'false'
    if a_list or b_list:
        return 'false'
    return 'true'


aa = solution('c,,')
print(aa)
