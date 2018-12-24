# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    nums, num = line.strip().split(' ')
    nums = nums.split(',')
    if num in nums:
        return nums.index(num)
    else:
        return -1


aa = solution('4,5,6,7,0,1,2 8')
print(aa)
