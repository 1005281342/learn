import unicodedata
import re

# 供应商携程 拼接属性 标识KEY 大部分有属性面积且格式如下
SplCtripIdentifier = 'area:'
SplCtripIdentifierCN = '面积:'
# 供应商携程过滤属性，属性一般拼接在后面并且有"("保护
SplCtripSplit = '('

# 英文字符集，26个英文字母，10个数字，空格字符
UsCharSet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', ' '}


# 去掉全部的变音符号
def shave_makes(txt) -> str:
    txt = txt or ''
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


# 处理西文字符
# BEGIN ASCIIZE
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  # <1>
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  # <2>
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})


# 一些常见西文字符转换
def dewinize(txt: str) -> str:
    txt = txt or ''
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  # <4>


# 去掉指定字符之间的字符串
def remove_strings_between_specified_characters(txt: str, character_pairs: tuple = ('(', ')')):
    """
        Agoda 城市字符串规范处理
    """
    if character_pairs is None or not character_pairs:
        return txt

    a, b = character_pairs
    index_a = txt.find(a)
    index_b = txt.find(b)

    if index_a < 0:  # 主要考虑到没查询到字符起点下标
        return txt
    elif index_b < 0:  # 未查询到字符终止下标
        return txt[:index_a]
    else:
        return txt[:index_a] + txt[index_b + 1:]


# 过滤字符, 增加对变音字符的处理[参考流畅的Python 4.6.3] todo 用于数据预处理 文本过滤
def str_filter_plus(a_string, character_pairs=None):
    # 过滤供应商携程拼接的属性
    if SplCtripIdentifier in a_string.lower():
        a_string = SplCtripSplit.join(a_string.split(SplCtripSplit)[:-1])
    if SplCtripIdentifierCN in a_string:
        a_string = SplCtripSplit.join(a_string.split(SplCtripSplit)[:-1])

    # 去掉指定字符之间的字符串
    a_string = remove_strings_between_specified_characters(a_string, character_pairs)

    # 要保留需要的字符
    def before_str_filter(before_string: str) -> str:
        maybe_dict = {
            '|': ' or ',
            ' ': 'oyjx',
            '&': ' and ',
            '/': ' or ',
            "\\": ' or ',
            '(': 'oyjx',
            ')': 'oyjx',
            "（": 'oyjx',
            "）": 'oyjx',
            "-": 'oyjx',
            "_": 'oyjx',
            ',': ' ',
            '，': ' ',
        }
        maybe_map = str.maketrans(maybe_dict)

        # key_list = ['&', '/', '\\', ' ', '-', '(', ')', "（", "）", "_"]
        # for key in key_list:
        #     if key in before_string:
        #         before_string = before_string.replace(key, maybe_dict[key])
        # print(before_string)

        # 使用 str 内置的 translate
        return before_string.translate(maybe_map)

    # 替换回空格字符 ' '， 并将多个空格字符压缩为一个空格字符
    def after_str_filter(after_string: str) -> str:
        after_string = after_string.replace('oyjx', ' ')
        return re.sub(' +', ' ', after_string)

    # step_1, 去掉变音字符
    a_string = dewinize(shave_makes(a_string))

    # step_2, 进行字符保留
    before_string = before_str_filter(a_string.lower())
    # print(string)

    # step_3, 过滤
    return after_str_filter(re.sub('[^\w\u4e00-\u9fff]+', '', before_string)).strip()


def strings_type_cn(strings: str) -> bool:
    # en_count, cn_count = 0, 0
    cn_count = 0
    strings = str_filter_plus(strings.lower())
    for char in strings:
        if char not in UsCharSet:
            cn_count += 1
    # return cn_count > 2 * en_count
    return cn_count > 2 or (len(strings) - cn_count <= 2)


if __name__ == '__main__':
    print(strings_type_cn("豪华大床房"))