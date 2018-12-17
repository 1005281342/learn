import string

# 几种字符串格式化的方式
values = {'var': 'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT:', s.format(**values))

"""

    In the first two cases, the trigger character ($ or %) is escaped by repeating it twice. 
    For the format syntax, both { and } need to be escaped by repeating them.
    在前面的两个例子，通过占位符'%'或'$'来格式化字符串，
    在python中使用 string的format类方法格式化更为简洁。
"""
