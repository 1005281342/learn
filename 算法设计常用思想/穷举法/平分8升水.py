from collections import deque


class WaterStatus(object):
    def __init__(self, limit, water):
        self.limit = limit  # 最大容量
        self.water = water  # 装水容量


def change_water(src: WaterStatus, dst: WaterStatus):
    if src.water == 0 or dst.water == dst.limit:
        water = 0
    if src.water >= dst.limit - dst.water:
        water = dst.limit - dst.water
    else:
        water = src.water
    src.water -= water
    dst.water += water


if __name__ == '__main__':
    a = WaterStatus(8, 8)
    b = WaterStatus(5, 0)
    c = WaterStatus(3, 0)
    water_list = [a, b, c]
    water_queue = deque()
    water_queue.append([8, 0, 0])

    cur_status = []
    cnt = 1
    while True:
        print('***第 %d 次循环***' % cnt)
        cnt += 1
        if [4, 4, 0] == cur_status:
            print('find it!')
            break
        for water1 in water_list:
            for water2 in water_list:
                # 记录当前状态，深拷贝deepcopy，创建新的对象
                cur_status = list(water_queue[-1])
                water_list[0].water = cur_status[0]
                water_list[1].water = cur_status[1]
                water_list[2].water = cur_status[2]
                # print water_list[0].water, water_list[1].water, water_list[2].water
                # 计算一次迁移
                if water1.limit != water2.limit:
                    change_water(water1, water2)
                    next_status = [water_list[0].water, water_list[1].water, water_list[2].water]
                    # print 'next_status' , next_status
                    if next_status in water_queue:
                        # print '迁移后的状态在记录中存在，将当前状态转到迁移之前的状态'
                        pass
                    else:
                        # print '记录迁移后的状态,一定要用list()来新建一个对象'
                        cur_status = next_status
                        water_queue.append(list(next_status))
                    # print water1.limit , water2.limit, cur_status
                    print('---', water_queue)
