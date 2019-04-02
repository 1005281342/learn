# class WP(object):
#
#     def __init__(self, wight, price):
#         self.wight = wight
#         self.price = price
#         self.status = 0
#
#     # 状态 0 未被选中
#
#
# obj_list = [WP(wight=w, price=p) for w, p in zip(Wi, Pi)]

W_Max = 150

Wi = [35, 30, 60, 50, 40, 10, 25]
Pi = [10, 40, 30, 50, 35, 40, 30]
# density = {i: p/w for i, (w, p) in enumerate(zip(Wi, Pi))}
density = [p / w for w, p in zip(Wi, Pi)]

index_list = []
while max(density) >= 0:

    Max = max(density)
    index = density.index(Max)
    if W_Max >= Wi[index]:
        W_Max -= Wi[index]
        density[index] = -1
        index_list.append(index + 1)
    else:
        density[index] = -2

print(index_list)
