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
    nums_add_10 = [x+10 for x in nums]
    count = 0
    for i in range(len(nums)):
        if nums[i] in nums_add_10:
            count += 1
            # print(nums[i])

        for j in range(i+1, len(nums)):

            if nums[i] + nums[j] == 10:
                count += 1
                # print(nums[i], nums[j])

    return str(count)


aa = solution("6,4,16")
print(aa)