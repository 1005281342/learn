# 最开始是在str类方法里看见 b""这个骚操作 定义字节序列
print(str.replace.__doc__)

# 尝试, wtf没报错
print(b"")

# 一堆数字就很真实，ASCII码
test_b = b"hello Python"
print(test_b)
for char in test_b:

    print(char)

# 然后python也提供了相关函数, 如果是Unicode字符

test_char = 'o'
number = ord(test_char)
print(number)

char = chr(number)
print(char)
