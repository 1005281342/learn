# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    nums = line.strip().split(',')
    count = 0
    for index in range(len(nums)-1):
        status = False
        for j in range(len(nums)-1 - index):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 1
                status = True
        if not status:
            return count
    return count


aa = solution('2,3,1')
print(aa)
