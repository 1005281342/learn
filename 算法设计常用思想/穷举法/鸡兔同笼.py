t = 50
j = 120
ji = 2
tu = 4

for tu_num in range(j // tu):

    if tu_num * tu + (t - tu_num) * ji == j:
        print(tu_num, t - tu_num)
