import types
from python.review.属性 import MoneyPlus


# 实例方法
def func(self):
    print("just func test")
    print(self.test)


"""
    静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，主要是一些逻辑属于类，但是和类本身没有交互，
    即在静态方法中，不会涉及到类中的方法和属性的操作。可以理解为将静态方法存在此类的名称空间中。
    事实上，在python引入静态方法之前，通常是在全局名称空间中创建函数
"""


# 添加静态方法
@staticmethod
def test_func():

    print("this is a staticmethod func test")


# 添加类方法
@classmethod
def test_func_plus(cls):

    print(cls.test)


t = type("t", (), {})
print(t())

t1 = type("t1", (MoneyPlus,), {})
print(t1())

t2 = type("t2", (MoneyPlus,), {"test": "this is type class test"})
print(t2())

MoneyPlusType = type("MoneyPlusType", (MoneyPlus,), {"test": "this is type class test",
                                                     "func": func,
                                                     "test_func": test_func,
                                                     "test_func_plus": test_func_plus,
                                                     })
M = MoneyPlusType()
print(M.func())
print("*"*10)
print(M.test_func())
print("*"*10)
print(M.test_func_plus())
print("*"*10)

print(M.__class__)  # <class '__main__.MoneyPlusType'> 类，实例化对象
print(MoneyPlusType.__class__)  # <class 'type'> 元类type,创建类的类

M_P = MoneyPlus()

# 增加实例方法
M_P.test = types.MethodType(func, M_P)

MoneyPlus.test = "测试"
# 增加静态方法
MoneyPlus.test_func = test_func

# 增加类方法
MoneyPlus.test_func_plus = test_func_plus

print(M_P.test())
MoneyPlus.test_func()
MoneyPlus.test_func_plus()
