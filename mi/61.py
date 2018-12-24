# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    nums_2 = [x.split(',') for x in line.strip().split(';')]
    for i in range(len(nums_2)):
        if nums_2[i] in nums_2[i+1:]:
            return str(i+1)+','+str(nums_2[i+1:].index(nums_2[i])+(i+1)+1)


aa = solution("1,0,0,1,0;0,1,1,0,0;0,0,1,1,0;1,0,0,1,0;0,1,0,0,0")
print(aa)
