import sys

for line in sys.stdin:
    line = line.strip()
    a, b, c, d, e = [int(g) for g in line.split(' ')]
    a, b, c = sorted([a, b, c])
    d, e = sorted([d, e])
    a_list = sorted([x1 ** 3 * a for x1 in range(-50, 51)])
    b_list = sorted([x2 ** 3 * b for x2 in range(-50, 51)])
    c_list = sorted([x3 ** 3 * c for x3 in range(-50, 51)])
    d_list = sorted([x4 ** 3 * d for x4 in range(-50, 51)])
    e_list = sorted([x5 ** 3 * e for x5 in range(-50, 51)])
    print(1)

    m = []
    for ee in e_list:
        for dd in d_list:
            m.append(ee + dd)

    n = set()
    for aa in a_list:
        for bb in b_list:
            for cc in c_list:
                n.add(aa + bb + cc)
    print(2)
    c = 0
    m.sort()

    print(len(m))
    print(len(n))
    for hh in m:
        if hh in n:
            c += 1
    print(c)
    # for x_1 in a_list:
    #     for x_2 in b_list:
    #         for x_3 in c_list:
    #             for x_4 in d_list:
    #                 ee = x_1 + x_2 + x_3 - x_4
    #                 if ee and ee in e_list:
    #                     s.add((a_list.index(x_1), b_list.index(x_2), c_list.index(x_3), d_list.index(x_4), e_list.index(ee)))
    #                 continue
