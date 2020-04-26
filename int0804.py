#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 1:16
# @Author  : Fhh
# @File    : int0804.py
# Good good study,day day up!
"""
幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。

说明：解集不能包含重复的子集。

示例:

 输入： nums = [1,2,3]
 输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        res = []

        def mi(tmp, n, arr):
            if len(tmp) == n:
                res.append(tmp)
                return
            else:
                for i in range(len(arr)):
                    if (not tmp or arr[i]>=tmp[-1]) and(i==0 or (i>0 and arr[i]>arr[i-1])):
                        mi(tmp + [arr[i]], n, arr[:i] + arr[i + 1:])

        for i in range(len(nums)+1):
            mi([], i, nums)
        return res
s=Solution()
print(s.subsets([1,1,2,3]))