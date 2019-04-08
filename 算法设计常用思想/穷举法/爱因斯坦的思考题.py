"""
题目描述：

    据说有五个不同颜色的房间排成一排，
    每个房间里分别住着一个不同国籍的人，
    每个人都喝一种特定品牌的饮料，
    抽一种特定品牌的烟，养一种宠物，
    没有任意两个人抽相同品牌的香烟，
    或喝相同品牌的饮料，或养相同的宠物，
    问题是谁在养鱼作为宠物？

线索：

    （1）英国人住在红色的房子里
    （2）瑞典人养狗作为宠物
    （3）丹麦人喝茶
    （4）绿房子紧挨着白房子，在白房子的左边
    （5）绿房子的主人喝咖啡
    （6）抽 Pall Mall 牌香烟的人养鸟
    （7）黄色房子里的人抽 Dunhill 牌香烟
    （8）住在中间那个房子里的人喝牛奶
    （9）挪威人住在第一个房子里面
    （10）抽 Blends 牌香烟的人和养猫的人相邻
    （11）养马的人和抽 Dunhill 牌香烟的人相邻
    （12）抽 BlueMaster 牌香烟的人喝啤酒
    （13）德国人抽 Prince 牌香烟
    （14）挪威人和住在蓝房子的人相邻
    （15）抽 Blends 牌香烟的人和喝矿泉水的人相邻
"""

from itertools import permutations
from copy import deepcopy

#  房子      国籍	    饮料	    宠物	    烟
# 初始化5个组 用以代表5个人以及5个属性
map_info = [
    [''] * 5 for _ in range(5)
]

# 根据线索9 得到
map_info[0][1] = '挪威'

# 根据 房间排成一排 与线索14 得到
map_info[1][0] = '蓝色'

# 根据 线索8 得到
map_info[2][2] = '牛奶'

# 线索绑定 s4 得到 绿色白色为一体
# 并且只能在2，3 或3，4位置，0开始
# s1 = ['红色', '英国', '', '', '']
# s2 = ['', '瑞典', '', '狗', '']
# s3 = ['', '丹麦', '茶', '', '']
# s5 = ['绿色', '', '咖啡', '', '']
# s6 = ['', '', '', '鸟', 'PallMall']
# s7 = ['黄色', '', '', '', 'Dunhill']
# s12 = ['', '', '啤酒', '', 'BlueMaster']
# s13 = ['', '德国', '', '', 'Prince']

#    # s11 10, 15

# 从颜色开始，绿白只能或3，4位置 绿房 喝 咖啡
# 2位置已经固定为牛奶了 s5
map_info[3][0] = '绿色'
map_info[3][2] = '咖啡'
map_info[4][0] = '白色'

# 结合国籍看 那么剩下颜色中间位置
map_info[2][0] = '红色'
map_info[2][1] = '英国'
map_info[0][0] = '黄色'
# print(map_info)
# todo ---以上 颜色排列完整

# s7 绑定 Dunhill
map_info[0][4] = 'Dunhill'
# s11 养马的人和抽 Dunhill 牌香烟的人相邻
map_info[1][3] = '马'
# print(map_info)


# 对剩下的7个线索做为消费数据对象
# 对剩下的4个类型作为排列对象生产数据


# 消费数据
def check(map_info_test):
    for i in range(5):

        if map_info_test[i][1] == '瑞典' and map_info_test[i][3] != '狗':
            return False
        if map_info_test[i][1] == '丹麦' and map_info_test[i][2] != '茶':
            return False
        if map_info_test[i][3] == '鸟' and map_info_test[i][4] != 'PallMall':
            return False
        if map_info_test[i][2] == '啤酒' and map_info_test[i][4] != 'BlueMaster':
            return False
        if map_info_test[i][1] == '德国' and map_info_test[i][4] != 'Prince':
            return False
        if map_info_test[i][4] == 'Blends':
            status = False
            try:
                if map_info_test[i - 1][3] == '猫':
                    status = True
            except:
                pass
            try:
                if map_info_test[i + 1][3] == '猫':
                    status = True
            except:
                pass
            if status is False:
                return False

        if map_info_test[i][4] == 'Blends':

            status = False
            try:
                if map_info_test[i - 1][2] == '水':
                    status = True
            except:
                pass
            try:
                if map_info_test[i + 1][2] == '水':
                    status = True
            except:
                pass
            if status is False:
                return False
    # 通过校验
    return True


# 生产数据
"""
1. 国籍 1，3，4 -- 丹麦、德国、瑞典
2. 饮料 0，1，4 -- 水、茶、啤酒
3. 宠物 0，2，3，4 -- 猫、鸟、鱼、狗
4. 烟 1，2，3，4 -- Blends、PallMall、Prince、BlueMaster
"""

res = []
for g in permutations({'丹麦', '德国', '瑞典'}, 3):
    map_info[1][1], map_info[3][1], map_info[4][1] = g
    # print(map_info)

    for yl in permutations({'水', '茶', ' 啤酒'}, 3):
        map_info[0][2], map_info[1][2], map_info[4][2] = yl

        for c in permutations({'猫', '鸟', '鱼', '狗'}, 4):
            map_info[0][3], map_info[2][3], map_info[3][3], map_info[4][3] = c

            for y in permutations({'Blends', 'PallMall', 'Prince', 'BlueMaster'}, 4):
                map_info[1][4], map_info[2][4], map_info[3][4], map_info[4][4] = y

                if check(map_info):
                    res.append(deepcopy(map_info))

for r in res:
    print(r)
