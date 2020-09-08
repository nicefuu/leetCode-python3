#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 22:56
# @Author  : Fhh
# @File    : int47.py
# Good good study,day day up!
"""

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？



示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物


提示：

0 < grid.length <= 200
0 < grid[0].length <= 200
"""
from functools import reduce
from typing import List
import time


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        res = []

        def go(i, j, sum):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                res.append(sum + grid[i][j])
                return
            else:
                if i < len(grid) - 1:
                    go(i + 1, j, sum + grid[i][j])
                if j < len(grid[0]) - 1:
                    go(i, j + 1, sum + grid[i][j])

        go(0, 0, 0)

        return max(res)


class Solution2:
    def maxValue(self, grid: List[List[int]]) -> int:
        def m(i, j, grid):
            if i == 0:
                return reduce(lambda x, y: x + y, grid[0][:j + 1])
            if j == 0:
                return reduce(lambda x, y: x + y, [grid[k][0] for k in range(i + 1)])
            else:
                return grid[i][j] + max(m(i - 1, j, grid), m(i, j - 1, grid))

        return m(len(grid) - 1, len(grid[0]) - 1, grid)


class Solution3:
    def maxValue(self, grid: List[List[int]]) -> int:
        def m(i, j, grid):
            if i == 0:
                tmp = 0
                for k in range(0, j + 1):
                    tmp += grid[0][k]
                return tmp
            if j == 0:
                tmp = 0
                for k in range(0, i + 1):
                    tmp += grid[k][0]
                return tmp
            else:
                return grid[i][j] + max(m(i - 1, j, grid), m(i, j - 1, grid))

        return m(len(grid) - 1, len(grid[0]) - 1, grid)


class Solution4:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = [[grid[0][0] for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            res[i][0] = res[i - 1][0] + grid[i][0]
        for j in range(1, n):
            res[0][j] = res[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = grid[i][j] + max(res[i - 1][j], res[i][j - 1])
        return res[m-1][n-1]



start = time.time()
s = Solution4()
a = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
for i in range(10000):
    s.maxValue(a)
# print(s.maxValue(a))
end = time.time()
print(round(end - start, 10))
