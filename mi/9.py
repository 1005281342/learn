# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    a, bb = line.strip().split(' ')
    b = int(bb)
    if '0' in a and b >= a.index('0'):
        return str(int(a[b:]))
    else:
        n = 0
        l = len(a)
        s = set()
        while n <= l-b:
            # s.add(int(a[n: n+l-b]))
            s.add(int(a[0: n] + a[n+b:]))
            n += 1
            print(s)
        return str(min(s))


aa = solution('1266 3')
print(aa)
