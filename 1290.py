# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum =[]
        while head:
            sum.append(str(head.val))
            head = head.next
        return int(''.join(sum),2)

head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
for i in range(len(head)):
    pass

s =Solution()
print(s.getDecimalValue(head))