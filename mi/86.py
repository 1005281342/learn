# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
#     import math

    num = int(line.strip())
    count = 0

    if num <= 1:
        return 'Bad'

    if num == 2:
        return 'Good'

    def log_2(x):
        if x % 2 != 0:
            return False

        while x > 1:
            x /= 2
            if x != int(x):
                return False
        return True

    # one = math.log(num-1, 2)
    # two = math.log(num+1, 2)
    one = log_2(num-1)
    two = log_2(num+1)
    if one:  # 1
        count += 3
    if two:
        count += 1
    if count == 4:
        return 'Very Good'
    elif count >= 3:
        return 'Good'
    elif count >= 1:
        return 'Bad'
    else:
        return 'Normal'


aa = solution('18014398509481985')
print(aa)
