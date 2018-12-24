
# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    base_dict = {')': '(', '}': '{', ']': '['}


    stack = []
    for char_ in line:
        if char_ in base_dict:
            top_element = stack.pop() if stack else ""

            if base_dict[char_] != top_element:
                return '0'
        else:
            stack.append(char_)

    if not stack:
        return '1'
    else:
        return '0'


aa = solution("(({[])}")
print(aa)
