#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 15:01
# @Author  : Fhh
# @File    : 229.py
# Good good study,day day up!
"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
示例 1:
输入: [3,2,3]
输出: [3]
示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        res = []
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict:
            if dict[i] > int(len(nums) / 3):
                res.append(i)
        return res


s = Solution()
print(s.majorityElement([1, 1, 1, 2, 2, 2, 3, 3]))
