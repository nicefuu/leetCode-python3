"""给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。

请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。
"""

import time


class Solution:  # 暴力法
    def oddCells(self, n, m, indices):
        """
        :param n:int 行
        :param m: int 列
        :param indices: list[list[int]]
        :return: int
        """
        a = []
        b = []
        for i in range(m):
            a.append(0)
        for j in range(n):
            b.append(a.copy())
        ci = len(indices)
        hang = list(zip(*indices))[0]
        lie = list(zip(*indices))[1]
        for i in hang:
            for j in range(m):
                b[i][j] += 1
        for i in lie:
            for j in range(n):
                b[j][i] += 1
        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] % 2 == 1:
                    cnt += 1
        return cnt


s = Solution()
print(s.oddCells(2, 2, [[1, 1], [0, 0]]))
