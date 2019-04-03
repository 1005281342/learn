p_m = 5
p_w = 3
p_x = 1 / 3

n = 100
for i in range(0, n // p_m):

    for j in range(0, n // p_w):

        if i * p_m + j * p_w + (100 - i - j) * p_x == 100:
            print(i, j, 100 - i - j)
