# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    a, b = line.strip().split(' ')

    a_set = [x for x in a]
    b_set = [x for x in b]
    while a_set:
        word = a_set.pop()
        if word in b_set:
            b_set.remove(word)
        else:
            return 'false'
    return 'true'


aa = solution('aa ab')
print(aa)


"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    a, b = line.strip().split(' ')

    a_set = {x for x in a}
    b_set = {x for x in b}
    if b_set.issuperset(a_set):
        return 'true'
    else:
        return 'false'


aa = solution('uak areuok')
print(aa)

"""