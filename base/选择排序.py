a = [2, 4, 3, 5, 7, 1, 8, 2]


# 每次选择最小的放在前面
def chose(b: list) -> list:
    for i in range(len(b) - 1):
        min_index = i
        for j in range(i + 1, len(b)):
            if b[j] < b[min_index]:
                b[j], b[min_index] = b[min_index], b[j]

    return b


b = chose(a)
print(b)
