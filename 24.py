"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :param head:ListNode
        :return: ListNode
        """
        if not head or head==None or head.next==None:
            return head
        node=head.next
        head.next=node.next
        node.next=head
        head=node
        #以上交换头结点与第二个结点
        node0=head.next
        while node0.next!=None:
            node1=node0.next
            if node1.next==None:
                break
            node2=node1.next
            node1.next=node2.next
            node2.next=node1
            node0.next=node2
            node0=node1
        return head
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :param head:ListNode
        :return: ListNode
        """
        node=ListNode(None)
        node.next=head
        node0=node
        while node0.next!=None:
            node1=node0.next
            if node1.next==None:
                break
            node2=node1.next
            node1.next = node2.next
            node2.next = node1
            node0.next = node2
            node0 = node1
        return node.next
