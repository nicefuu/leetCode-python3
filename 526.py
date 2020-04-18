#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 16:12
# @Author  : Fhh
# @File    : 526.py
# Good good study,day day up!
"""假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？
示例1:
输入: 2
输出: 2
解释:
第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除
第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
说明:
N 是一个正整数，并且不会超过15。
"""


class Solution:
    def countArrangement(self, N: int) -> int:
        """
        :param N:int
        :return: int
        """
        res = []

        def backtrack(arr, n):
            if len(arr) == N:
                res.append(arr)
                return
            for i in range(1, N + 1):
                if i not in arr and (i % n == 0 or n % i == 0):
                    backtrack(arr + [i], n + 1)
            return

        for i in range(1, N + 1):
            backtrack([i], 2)
        return len(res)


s = Solution()
for i in range(1,16):
    print(s.countArrangement(i))
