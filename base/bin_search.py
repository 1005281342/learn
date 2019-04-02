def bin_search(nums, num):
    left = 0
    right = len(nums) - 1
    while left <= right:

        mid = (left + right) >> 1
        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            left = mid+1
        else:
            right = mid-1
    return -1


print(bin_search(list(range(1, 10)), 0))
