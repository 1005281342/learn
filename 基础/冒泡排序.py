"""

    冒泡排序
    时间复杂度：O(n^2)
    稳定性：稳定
    改进：如果一趟比较没有发生位置变换，则认为排序完成

    常用七种排序的python实现        https://www.cnblogs.com/zingp/p/6537841.html#_label4
"""


def bubble_sort(array):
    for i in range(len(array)-1):
        current_status = False
        for j in range(len(array) - i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                current_status = True
        if not current_status:
            break
