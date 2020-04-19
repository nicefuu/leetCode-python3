#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 19:42
# @Author  : Fhh
# @File    : 33.py
# Good good study,day day up!
"""假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution:
    def search(self, nums, target: int) -> int:
        """
        :param nums: list[int]
        :param target: int
        :return: int
        """
        if not nums or len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return -1
        index = 0
        if target >= nums[index]:
            while index < len(nums):
                if nums[index] == target:
                    return index
                if nums[index] > target or (index < len(nums) - 1 and nums[index + 1] < nums[index]):
                    return -1
                index += 1
        else:
            index = len(nums) - 1
            while index>0:
                print(index)
                if nums[index] == target:
                    return index
                if nums[index] < target or (index > 0 and nums[index - 1] > nums[index]):
                    return -1
                index -= 1
        return -1


s = Solution()
print(s.search([1,3], 0))
