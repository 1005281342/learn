nums = [1, 5, 7, 9, 3, 2, 1, 5]


# def quick_sort(array, left, right):
#
#     if left < right:
#
#         mid = partition(array, left, right)
#         quick_sort(array, left, mid-1)
#         quick_sort(array, mid+1, right)
#
# def partition(array, left, right):


def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid - 1)
        quick_sort(array, mid + 1, right)


def partition(array, left, right):
    tmp = array[left]
    while left < right:
        # 保证子序列中右边的数都比左边的大，右指针左移
        while left < right and array[right] >= tmp:
            right -= 1
        array[left] = array[right]

        # 保证子序列中左边的数都比右边的小，左指针右移
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]

    array[left] = tmp
    # print(nums)
    return left


quick_sort(nums, 0, 7)
print(nums)
