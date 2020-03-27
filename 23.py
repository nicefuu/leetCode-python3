"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
a1.next = a2
a2.next = a3
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3
c1 = ListNode(2)
c2 = ListNode(6)
c1.next = c2


class Solution:
    def mergeKLists(self, lists):
        """
        :param lists:list[ListNode]
        :return: ListNode
        """
        if len(lists)==0:
            return None
        temp=[]
        for i in range(len(lists)):
            node = lists[i]
            while node != None:
                temp.append([node.val,node])
                node = node.next
        if not temp or len(temp)==0:
            return None
        temp.sort(key=lambda temp:temp[0])
        for i in range(len(temp)-1):
            temp[i][1].next=temp[i+1][1]
        return temp[0][1]
s = Solution()
node=s.mergeKLists([a1, b1, c1])
while node!=None:
    print(node.val)
    node=node.next

