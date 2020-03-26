"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
from listNodeTest import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
sl = single_list(a)


class Solution:
    def reverseBetween(self, head, m: int, n: int):
        if m == 1:
            node = head
            for i in range(n-m):
                temp = node.next
                node.next = temp.next
                print("val={}".format(temp.next.val))
                temp.next = head
                head = temp

            return head
        elif m > 1:
            node = head
            for i in range(m - 1):
                if i == m - 2:
                    left = node
                node = node.next
            for i in range(n - m):
                temp = node.next
                node.next = temp.next
                temp.next = left.next
                left.next = temp
            return head


s = Solution()
s.reverseBetween(a,1,4)
for i in range(5):
    print(str(sl.search(i).val)+" ",end='')
