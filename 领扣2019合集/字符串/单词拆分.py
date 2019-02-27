from itertools import combinations


def indexCombinations(s):
    ret = []
    for i in range(1, len(s)):
        index_combs = combinations([i for i in range(1, len(s) - 1)], i)  # 获取拆分为i段的下标组合
        ret.extend(index_combs)
    return ret


def wordBreak(words, dt):
    res = []
    for item in indexCombinations(words):
        current = 0
        tmp = []
        for i in item:
            tmp.append(words[current:i])  # 获取每一段
            current = i
        tmp.append(words[current:])  # 收尾
        if set(tmp).issubset(set(dt)):  # 判断是否在给定字典里面。set函数去重导致的问题不大
            res.append(' '.join(tmp))
    return res
