#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 12:45
# @Author  : Fhh
# @File    : 59.py
# Good good study,day day up!
"""给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
通过次数
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        i = 1
        direction = "right"
        while 1:
            if i == n * n + 1:
                break
            if res[x][y] == 0:
                res[x][y] = i
                i += 1
            if direction == "right":
                # print("1")
                if y == n - 1 or res[x][y + 1] != 0:
                    x += 1
                    direction = "down"
                else:
                    y += 1
            elif direction == "down":
                # print("2")
                if x == n - 1 or res[x + 1][y] != 0:
                    y -= 1
                    direction = "left"
                else:
                    x += 1
            elif direction == "left":
                # print("3")
                if y == 0 or res[x][y - 1] != 0:
                    x -= 1
                    direction = "up"
                else:
                    y -= 1
            else:
                # print("4")
                if x == 0 or res[x - 1][y] != 0:
                    y += 1
                    direction = "right"
                else:
                    x -= 1

        return res


s = Solution()
for i in s.generateMatrix(5):
    print(i)
