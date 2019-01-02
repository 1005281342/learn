# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'
    a, b = line.strip().split('-')

    return str(int(a)-int(b))

    # a_list = [int(x) for x in a]
    # b_list = [int(x) for x in b]
    # c = len(a_list) - len(b_list)
    #
    # s = []
    # status = 0
    # while b_list:
    #
    #     if status:
    #         a_list[-1] -= 1
    #         status = 0
    #     b_num = b_list.pop()
    #     a_num = a_list.pop()
    #     cc = a_num-b_num
    #     if cc >= 0:
    #         s.append(cc)
    #     else:
    #         s.append(10+c)
    #         status = 1
    #
    # if c > 1 and status:
    #     if a_list[c - 1] == 0:
    #         a_list[c - 1] += 10
    #         a_list[c - 2] -= 1
    #         status = 0
    # n = 2
    #
    # while n < c and status:
    #     if a_list[c - n] < 0:
    #         a_list[c - n] += 10
    #         a_list[c - n - 1] -= 1
    #         status = 0
    #     n += 1
    #
    # s.reverse()
    # if a_list and a_list[0] == 0:
    #     a_list.remove(0)
    #
    # ss = a_list + s
    # s_s = ''
    # for x in ss:
    #     s_s += str(x)
    # return s_s


    # 对被减数检测

    # for i in range(1, len(b)+1):
    #     aa = int(a[-i])
    #     if status:
    #         aa = aa - 1     # 是否有被借位
    #         status = 0
    #     bb = int(b[-i])
    #     if aa >= bb:
    #         s.append(str(aa-bb))
    #     else:
    #         s.append(str(10+aa-bb))
    #         status = 1
    #
    # # 0->b),b b+1 -> a)
    # x = 1
    # while x < len(a)-len(b):
    #     if status:
    #         aaa = int(a[-len(b)-x])
    #         if aaa > 0:
    #             a[-len(b)-x] = str(aaa - 1)
    #             status = 0
    #         x += 1
    #     else:
    #         break
    #
    # for j in range(1, x):
    #     a[-len(b)-x] = '9'
    #
    # s.reverse()
    # return a[:-len(b)] + ''.join(s)


if __name__ == '__main__':

    aa = solution("1231231237812739878951331231231237812739878951331231231237812739878951331231231237812739878951331231231237812739878951331231231237812739870-89513312312312378127398789513312312312378127398789513312312312378127398789513")
    print(aa)