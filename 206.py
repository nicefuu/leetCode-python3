"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
import listNodeTest


class Solution:
    def reverseList(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            node = head
            while node.next != None:
                temp = node.next
                node.next = temp.next
                temp.next = head
                head = temp
            return head
