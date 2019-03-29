#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (32.36%)
# Total Accepted:    35.9K
# Total Submissions: 109.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def get_length(self, head: ListNode):
        c = 0
        pre = head
        while pre.next is not None:
            c += 1
            pre = pre.next
        return c

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        c = self.get_length(head)
        if c <= 1:
            head = head.next
            return head
        index = c-n
        i = 0
        pre = head
        while pre.next is not None:
            if i == index:
                pre.next = pre.next.next
                break
            pre = pre.next
            i += 1
        return head
