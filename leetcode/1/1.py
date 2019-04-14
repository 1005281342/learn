from itertools import permutations


# 是否可查找
def is_can(x, y):
    return set(x) | set(y) == set(x)


# 源的子串
def perm(x):
    res = set()
    length = len(x)
    for x in range(1, length + 1):
        pp = permutations(range(length), x)
        c = 0
        while c < length + 1 - x:
            try:
                val = [str(b) for b in list(next(pp))]
            except:
                break
            if sorted(val) == val:
                c += 1
                res.add(''.join(val))
    return res


# score_string = 'abc'
# score_dict = {str(i): v for i, v in enumerate(score_string)}
#
# res = perm(score_string)
#
#
# def map_p(res):
#     res_p = set()
#     for cc in res:
#         res_p.add(''.join([score_dict[c] for c in cc]))
#     return res_p
#
#
# pp = sorted(list(map_p(res)), key=len, reverse=True)
# print(pp)


def tan_xin(score: str, target: str):
    # 不能被查找
    if not is_can(score, target):
        return -1

    score_dict = {str(i): v for i, v in enumerate(score)}
    t_len = len(target)
    z_res = perm(score)

    def map_p(res):
        res_p = set()
        for cc in res:
            res_p.add(''.join([score_dict[c] for c in cc]))
        return res_p

    pp = sorted(list(map_p(z_res)), key=len, reverse=True)
    # print(pp)
    count = 0
    for p in pp:
        # print(target)
        if target:
            target = target.replace(p, '')
            count += (t_len - len(target)) // len(p)
            t_len = len(target)
            # print(count)
        else:
            break
    if target:
        return -1
    return count


aa = tan_xin("xyz", "xzyxz")
print(aa)
