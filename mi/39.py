# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'

    aa = [[int(a) for a in x.split(',')] for x in line.strip().split(';')]
    print(aa)
    m = len(aa)
    n = len(aa[0])
    s = set()
    for i in range(m-1):

        for j in range(n-1):
            s.add(aa[i][j] + aa[i+1][j+1])

    return max(s)


aaa = solution("0,0;0,0")
print(aaa)
