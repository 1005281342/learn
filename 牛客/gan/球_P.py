import sys
from math import sqrt

Pi = 3.14

n = int(sys.stdin.readline().strip())


def br(num):
    return float(format(num, '.2f'))


def get_r_v(nums):

    nums = [br(x) for x in nums]
    r = format(
        sqrt(br((nums[4]-nums[1])**2) + br((nums[5] - nums[2])**2) + br((nums[3] - nums[0])**2)),
        '.2f')
    v = format(4 / 3 * Pi * (float(r) ** 3), '.2f')
    print(r, v)


for _ in range(n):
    nums = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    get_r_v(nums)
