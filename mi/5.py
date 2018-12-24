# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    words = [int(x) for x in line.strip().split(',')]

    words.sort()    # ['10', '12', '13', '14', '5', '6', '7', '8', '9']

    b = (len(words)-1)//2
    return words[b]


a = solution('12,13,14,5,6,7,8,9,10')
print(a)