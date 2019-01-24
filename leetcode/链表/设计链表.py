"""

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

"""


class MyLinkedList:

    def __init__(self, val=None, c_next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = c_next

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        count = 0
        cur = self

        while cur and (count <= index):
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        # head = MyLinkedList()
        tmp_val = self.val
        tmp_next = self.next
        self.val = val
        self.next = MyLinkedList(val=tmp_val, c_next=tmp_next)

        return self

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        m = MyLinkedList(val, None)
        p_next = self.next
        while p_next:

            if p_next.next is None:
                p_next.next = m
                return self
            p_next = p_next.next
        self.next = m
        return self

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

        m = MyLinkedList(val=val)
        if index == 0:
            return self.addAtHead(val=val)

        count = 1
        cur = self
        while count <= index and cur:

            if count == index:
                tmp = cur.next  # 下个节点
                cur.next = m
                m.next = tmp
            cur = cur.next
            count += 1
        return self

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # if index == 0:
        #     self.val = self.next.val
        #     self.next = self.next.next

        count = 0
        cur = self
        while count <= index and cur:

            if count == index:
                tmp = cur.next

                if tmp:
                    cur.val = tmp.val
                    cur.next = tmp.next

                # # 如果是最后一个节点
                # cur.next = None
                return self
            cur = cur.next
            count += 1

# Your MyLinkedList object will be instantiated and called as such:
val = 20
obj = MyLinkedList(2)
obj.addAtHead(12)
print(obj.val)
print(obj.next)

print("*"*10)
# print(obj.val)
# print(obj.next)

C = obj.addAtTail(val)
# print(C.val)
# print(C.next)
# print(C.next.val)
# print(C.next.next)

obj.addAtIndex(index=3, val=25)
print(obj.val)
print(obj.next.val)
print(obj.next.next.val)
print(obj.next.next.next.val)
print("*"*10)
obj.deleteAtIndex(index=2)
print(obj.val)
print(obj.next.val)
print(obj.next.next.val)
print("*"*10)
print(obj.get(2))
# print(B.next.next.val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
