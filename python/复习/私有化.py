"""

    _x: 单前置下划线,私有化属性或⽅法， from somemodule import *禁⽌导⼊,类对象和⼦类可以访问
    __xx： 双前置下划线,避免与⼦类中的属性命名冲突， ⽆法在外部直接访问(名字重整所以访问不到)
"""


class Test(object):

    def __init__(self):

        self.__age = 18
        self.__name = "o"

    def print_age(self):

        print(self.__age)

    def __print_name(self):

        print(self.__name)


C = Test()
# print(C.__age)
C.__age = 100
print(C.__age)

# 名字重整, 把原来的私有属性改成 "_"+"类名"+"私有属性名"
print(C._Test__age)

C.print_age()  # 18
# C.__print_name()

