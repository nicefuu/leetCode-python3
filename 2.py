"""给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        lastnode = ListNode(None)
        tmp = 0
        while node1 != None and node2 != None:
            node1.val += node2.val + tmp
            if node1.val >= 10:
                node1.val -= 10
                tmp = 1
            else:
                tmp = 0
            lastnode = node1
            node1 = node1.next
            node2 = node2.next
        if node1 == None and node2 == None:
            if tmp == 1:
                lastnode.next = ListNode(1)
            return l1
        elif node1 == None and node2 != None:
            lastnode.next = node2
            if tmp == 1:
                while node2 != None:
                    node2.val += tmp
                    if node2.val == 10:
                        node2.val = 0
                        tmp=1
                        if node2.next == None:
                            node2.next = ListNode(1)
                            break
                    else:
                        tmp=0
                    node2 = node2.next
            return l1
        else:  # node1 != None and node2 == None:
            if tmp == 1:
                while node1 != None:
                    node1.val += tmp
                    if node1.val == 10:
                        node1.val = 0
                        tmp=1
                        if node1.next == None:
                            node1.next = ListNode(1)
                            break
                    else:
                        tmp=0
                    node1 = node1.next
            return l1
