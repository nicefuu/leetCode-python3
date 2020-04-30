#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 22:44
# @Author  : Fhh
# @File    : 47.py
# Good good study,day day up!
"""给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = []
        n = len(nums)
        nums.sort()

        def func(tmp, n, arr):
            if len(tmp) == n:
                res.append(tmp)
                return
            for i in range(len(arr)):
                if i == 0 or (i > 0 and arr[i] != arr[i - 1]):#去重
                    func(tmp + [arr[i]], n, arr[:i] + arr[i + 1:])
        func([], n, nums)
        return res


s = Solution()
print(s.permuteUnique([1, 1, 1, 1]))
