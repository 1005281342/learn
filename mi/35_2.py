"""

题目
【1】把M个同样的苹果放在N个同样的盘子里,允许有的盘子空着不放,共有多少种分法
其实问题【1】已经有很多帖子写解法了,想知道剩下问题【2】【3】【4】的做法,求共有多少种方法
【2】把M个同样的苹果放在N个不同的盘子里,允许有的盘子空着不放
【3】把M个不同的苹果放在N个同样的盘子里,允许有的盘子空着不放
【4】把M个不同的苹果放在N个不同的盘子里,允许有的盘子空着不放


优质解答
    2.盘子是不一样的,相当于m+n个位置放n个盘子,而且最后一个位置必须是盘子.这样,每个盘子之前有几个空位,就是有几个苹果,
        于是=C（m+n-1）（n-1）
    3.苹果不同盘子相同太难 做不出来 用计算机搞一搞或许行
    4.不同的苹果 不同的盘子,每一个苹果都有n个选择放入,而且全不相同,于是=n^m


##问题描述：把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问有多少种不同的分法？(注：5,1,1和1,1,5是同一种分法)

解题分析：

　　设f(m,n)为m个苹果，n个盘子的放法数目，则先对n作讨论，

当n>m：则必定有n-m个盘子永远空着，去掉它们对摆放苹果方法数目不产生影响。即 if(n>m) f(m,n) = f(m,m)
当n <= m:不同的放法可以分成两类：含有0的方案数，不含有0的方案数
含有0的方案数，即有至少一个盘子空着，即相当于 f(m,n)=f(m,n-1);
不含有0的方案数，即所有的盘子都有苹果，相当于可以从每个盘子中拿掉一个苹果，不影响不同放法的数目，即 f(m,n)=f(m-n,n).而总的放苹果的放法数目等于两者的和，即 f(m,n)=f(m,n-1)+f(m-n,n)
递归出口条件说明：

当n=1时，所有苹果都必须放在一个盘子里，所以返回1；
当m==0(没有苹果可放)时，定义为1种放法；

"""


def f(m, n):

    if m == 0 or n == 1:
        return 1

    if n > m:
        return f(m, m)
    else:
        return f(m, n-1) + f(m-n, n)


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here

    # return 'your_answer'

    m_t, n_k = line.strip().split(' ')
    return f(int(m_t), int(n_k))


if __name__ == '__main__':

    aa = solution("5 2")
    print(aa)
