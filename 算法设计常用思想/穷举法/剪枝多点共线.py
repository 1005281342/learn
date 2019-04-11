from collections import Counter


def get_most_count(spot_list):
    res = set()
    length = len(spot_list)
    for j in range(length - 1):
        tmp = list()
        for i in range(j+1, length):
            x, y = spot_list[i]
            x0, y0 = spot_list[j]
            # 注意x==x0时的情况为斜率不存在
            if (x - x0) != 0:
                tmp.append(format((y - y0) / (x - x0), '.8f'))
            else:
                tmp.append(float("inf"))
        res.add(max(Counter(tmp).values()))
    return max(res) + 1


lst = [(1, 1), (2, 2), (3, 3), (6, 6), (0, 0), (1, 5), (1, 6), (1, 7), (1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (6, 6),
       (0, 0), (1, 5), (1, 6), (1, 7), (1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (6, 6), (0, 0), (1, 5), (1, 6), (1, 7),
       (1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (6, 6), (0, 0), (1, 5), (1, 6), (1, 7), (1, 3), (1, 2), (1, 1), (2, 2),
       (3, 3), (6, 6), (0, 0), (1, 5), (1, 6), (1, 7), (1, 3), (1, 2), (1, 1), (2, 2), (3, 3), (6, 6), (0, 0), (1, 5),
       (1, 6), (1, 7), (1, 3), (1, 2)]
s = get_most_count(lst)
print(len(lst))
print(s)
