# 给有序数组外排

a_list = [2, 4, 5, 7, 9]
b_list = [1, 6, 8, 12]
res = []

a_index = b_index = 0
while a_index < len(a_list) and b_index < len(b_list):

    if a_list[a_index] < b_list[b_index]:
        res.append(a_list[a_index])
        a_index += 1
    else:
        res.append(b_list[b_index])
        b_index += 1

# 将剩下的元素拷贝过来
res += a_list[a_index:] + b_list[b_index:]
print(res)
