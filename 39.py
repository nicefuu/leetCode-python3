#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/19 20:37
# @Author  : Fhh
# @File    : 39.py
# Good good study,day day up!
"""给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target: int):
        """
        :param candidates: list[int]
        :param target: int
        :return: list[list[int]]
        """
        res = []
        candidates.sort()

        def sumarr(arr):
            if not arr or len(arr) == 0:
                return 0
            else:
                sum = 0
                for i in range(len(arr)):
                    sum += arr[i]
                return sum

        res = []

        def dfs(tmp, arr, index, target):
            for i in range(index, len(arr)):
                if sumarr(tmp) + arr[i] == target:
                    tmp += [arr[i]]
                    res.append(tmp)
                    return
                elif sumarr(tmp) + arr[i] < target:
                    dfs(tmp + [arr[i]], arr, i, target)
                else:
                    return

        dfs([], candidates, 0, target)
        return res


s = Solution()
print(s.combinationSum([2, 3, 4], 12))
