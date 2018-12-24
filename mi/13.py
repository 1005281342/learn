# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
# 缩进请使用 4 个空格，遵循 PEP8 规范
# please write your code here

# return 'your_answer'
    list_str, top = line.strip().split(' ')
    top = int(top)
    tmp_dict = {}
    num_list = list_str.split(',')
    for num in num_list:
        num = int(num)
        if tmp_dict.get(num) is None:
            tmp_dict[num] = 1
        else:
            tmp_dict[num] += 1

    tmp = {}
    for key, value in tmp_dict.items():
        if tmp.get(value) is None:
            tmp[value] = [key, ]
        else:
            tmp[value].append(key)
    a = list(tmp.keys())
    a.sort()
    n = 0
    res = ''
    while a and n < top:
        a_num = a.pop()
        tmp[a_num].sort()
        for item in tmp[a_num]:
            res = res + str(item) + ','
            n += 1
            if n >= top:
                return res[:-1]


aa = solution('1,1,1,2,2,2,3 3')
print(aa)