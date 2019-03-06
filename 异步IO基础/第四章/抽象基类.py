# 检查某个类是否有某种方法
class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


#   1. 使用hasattr
com = Company([1, 2, 3])
print(hasattr(com, "__len__"))

#   2. 判断某个对象的类型
from collections.abc import Sized

print(isinstance(com, Sized))

#   3. 需要强制某个子类必须实现某些方法