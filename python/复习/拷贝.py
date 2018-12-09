# 浅拷贝, 把地址拷贝过去
a = [1, 2, 3]
b = a

# 深拷贝, 递归拷贝
import copy

"""
    额外开辟空间, 则会产生一个id
    
    copy.copy
        懒惰拷贝，如果是可变类型也会额外开辟空间，
        但是像元祖这种不可变类型则不会额外开辟空间。
        如果操作的第一层类型是可变类型，则只拷贝一层，
        如果操作的第一层类型是不可变类型，则不拷贝
        
    copy.deepcopy
        递归拷贝
        会额外开辟空间
        
"""
c = copy.copy(a)
d = copy.deepcopy(a)
print(id(c))
print(id(a))
print(id(d))


a.append(123)
print(a, b, c, d)

aa = [11, 22, 33]
bb = [44, 55, 66]

cc = [aa, bb]
dd = cc
ee = copy.copy(cc)
ff = copy.deepcopy(cc)
aa.append(100)
print(cc)
print(dd)
print(ee)
print(ff)

aaa = (1, 2)
bbb = (3, 4)
ccc = (aa, bb)
ddd = copy.copy(ccc)
eee = copy.deepcopy(ddd)
print(id(ccc))
print(id(ddd))
print(id(eee))
