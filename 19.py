"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :param head:ListNode
        :param n: int
        :return: ListNode
        """
        if n <= 0:
            return head
        else:
            cnt = 0
            node = head
            while node != None:
                cnt += 1
                node = node.next
            if n == cnt:
                head = head.next
            elif n > cnt:
                return head
            else:
                a = cnt - n
                k = 0
                node = head
                while k < a - 1:
                    node = node.next
                    k += 1
                node.next = node.next.next
        return head


class Solution2:  # 一次扫描实现
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :param head:ListNode
        :param n: int
        :return: ListNode
        """
        if n <= 0 or head == None:
            return head
        else:
            cnt = 0
            delnode = None
            node = head
            while node != None:
                cnt += 1
                if cnt == n + 1:
                    delnode = head
                elif cnt > n + 1:
                    delnode = delnode.next
                node = node.next
            if n >= cnt:
                head = head.next
            else:
                delnode.next = delnode.next.next
            return head


s = Solution2()
s.removeNthFromEnd(a, 7)
node = a
while node != None:
    print(node.val, end=" ")
    node = node.next
