#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 14:43
# @Author  : Fhh
# @File    : 83.py
# Good good study,day day up!
"""给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
            return head
        node=head
        while node.next !=None:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head