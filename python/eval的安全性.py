import ast

# print(eval("__import__('os').system('ls')"))

# todo ValueError: malformed node or string: <_ast.Call object at 0x10f4e69b0>
# print(ast.literal_eval("__import__('os').system('ls')"))

print(ast.literal_eval("{2: 4}"))
