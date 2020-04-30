#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 16:12
# @Author  : Fhh
# @File    : 1314.py
# Good good study,day day up!
"""给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:  # 超时
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat:
            return [[0]]
        __x = len(mat)
        __y = len(mat[0])

        def sumblock(x, y, mat, k):
            res = 0
            try:
                for i in range(x - k, x + k + 1):
                    for j in range(y - k, y + k + 1):
                        if (0 <= i < __x) and (0 <= j < __y):
                            res += mat[i][j]
            except:
                print("i={},j={}".format(i, j))
            return res

        r = [[0 for y in range(__y)] for x in range(__x)]
        for i in range(__x):
            for j in range(__y):
                r[i][j] = sumblock(i, j, mat, K)
        return r


class Solution2:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        x = len(mat)
        y = len(mat[0])
        p = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + mat[i - 1][j - 1]
        print(p)

        def getp(i, j):
            i = max(min(i, x), 0)
            j = max(min(j, y), 0)
            return p[i][j]

        ans = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                ans[i][j] = getp(i + K + 1, j + K + 1) - getp(i + K + 1, j - K) - getp(i - K, j + K + 1) + getp(i - K,
                                                                                                                j - K)
        return ans


class Solution3:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
        print(P)

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K,
                                                                                                            j - K)
        return ans


s2 = Solution2()
s3 = Solution3()
import time

print(s2.matrixBlockSum(mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], K=1))
print(s3.matrixBlockSum(mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], K=1))
