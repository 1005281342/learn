def climb_stairs(n):
    way = [0, 1, 2]
    for i in range(3, n + 1):
        way.append(way[i - 1] + way[i - 2])
    return way[n]


def easy_climb(n):
    return easy_climb(n - 1) + easy_climb(n - 2) if n not in [0, 1, 2] else n


print(easy_climb(9))
