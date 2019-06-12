# 判断字符串为None或为空字符串
def is_none_or_null(string) -> bool:
    return (string is None) or (len(str(string).replace(' ', '')) == 0)


# none_to_string
def none_to_string(a):
    return '' if is_none_or_null(a) else a


if __name__ == '__main__':
    print(none_to_string(''))
    print(none_to_string('aaa'))
    print(none_to_string(None))
    print(none_to_string('aaa'))
