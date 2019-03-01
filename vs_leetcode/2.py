#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.69%)
# Total Accepted:    86.8K
# Total Submissions: 265.7K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def chain_table_to_int(self, x: ListNode):
        s = ''
        while x:
            s += str(x.val)
            x = x.next
        if s:
            print(s)
            return int(s[::-1])
        else:
            return 0

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):

        return [int(x) for x in str(self.chain_table_to_int(l1) + self.chain_table_to_int(l2))[::-1]]

# class Solution:
#
#     def chain_table_to_int(self, x: ListNode):
#         s = ''
#         while x and x.next:
#             s += str(x.val)
#             x = x.next
#         if s:
#             return int(s[::-1])
#         else:
#             return 0
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode):
#
#         return [int(x) for x in str(self.chain_table_to_int(l1) + self.chain_table_to_int(l2))[::-1]]
