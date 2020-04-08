#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 21:32
# @Author  : Fhh
# @File    : 912.py
# Good good study,day day up!
"""给你一个整数数组 nums，请你将该数组升序排列。
示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

提示：
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""


class Solution:
    def sortArray(self, nums):
        """
        :param nums:list[int]
        :return: list[int]
        """
        counts = [0 for _ in range(100001)]
        for i in nums:
            counts[i + 50000] += 1
        res = []
        for i in range(100001):
            res += [i - 50000] * counts[i]
        return res


s = Solution()
print(s.sortArray([5, 4, 3, 2, 1, 1, -1, -2, -5]))
#  0  1  2  3  4 5 6 7 8 9 10
# -5 -4 -3 -2 -1 0 1 2 3 4 5
