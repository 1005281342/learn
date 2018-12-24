# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    nums = [int(x) for x in line.strip().split(',')]
    nums.sort()
    l = len(nums)
    s = set()
    for i in range(l-3):

        for j in range(i+1, l-2):

            if -(nums[i] + nums[j]) in nums[j+1:]:
                s.add((nums[i], nums[j]))

    return len(s)


aa = solution("-1,0,1,2,-1,-4")
print(aa)
