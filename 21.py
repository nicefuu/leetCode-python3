"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
a=ListNode(1)
b=ListNode(2)
c=ListNode(4)
d=ListNode(2)
e=ListNode(3)
f=ListNode(4)
# a.next=b
# b.next=c
# d.next=e
# e.next=f
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            temp = l2
            l2 = l2.next
            while temp != None:
                if temp.val <= l1.val:
                    temp.next = l1
                    l1 = temp
                else:
                    left = l1
                    if left.next==None:
                        l1.next=temp
                    else:
                        while temp.val > left.next.val:
                            left=left.next
                            if left.next==None:
                                break
                        temp.next=left.next
                        left.next=temp
                temp = l2
                if temp==None:
                    break
                l2 = l2.next
            return l1
s=Solution()
s.mergeTwoLists(a,d)
node=a
while(node.next!=None):
    print(node.val)
    node=node.next