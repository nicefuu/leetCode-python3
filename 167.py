#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 11:11
# @Author  : Fhh
# @File    : 167.py
# Good good study,day day up!
"""给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :param numbers:list[int]
        :param target: int
        :return: list[int]
        """
        if not numbers or len(numbers) < 2:
            return []

        def search(arr, x, index):  # 在arr中找到x并返回他的索引(且不等于i）
            if len(arr) == 0:
                return None
            for i in range(len(arr)):
                if i!=index:
                    if arr[i] == x:
                        return i
                    elif arr[i] > x:
                        return None
            return None

        for i in range(len(numbers)):
            if i-1>=0 :
                if numbers[i]==numbers[i-1]:
                    continue
            if search(numbers, target - numbers[i],i) != None:
                return [i + 1, search(numbers, target - numbers[i],i) + 1]
        return []


s = Solution()
print(s.twoSum([5,25,75], 100))
