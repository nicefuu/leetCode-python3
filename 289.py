#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 19:05
# @Author  : Fhh
# @File    : 289.py
# Good good study,day day up!
""""""
from typing import List


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 把board转化成3位2进制数第一位表示此次扫描是否变化过，第二位表示前一时刻状态，第三位表示当前时刻状态
        "初始化"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    board[i][j] = '000'
                else:
                    board[i][j] = '001'
        # print(board)

        def chage(i, j, board):
            res = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(board) and 0 <= y < len(board[0]):
                        key = board[x][y][2] if board[x][y][0] == '0' else board[x][y][1]
                        if key == '1':
                            res += 1
            if board[i][j][2] == '1':#如果该位置为存活则活细胞数-1（由于上面统计的是9个格子的活细胞数）
                res -= 1
            if board[i][j][2] == '1' and (res < 2 or res > 3):  # board[i][j]是活细胞且周围细胞小于2或大于3 则死亡
                board[i][j] = '110'
            elif board[i][j][2] == '1' and (res == 2 or res == 3):  # board[i][j]是活细胞且周围细胞为2或3 则仍然存活
                board[i][j] = '111'
            elif board[i][j][2] == '0' and res == 3:  # board[i][j]是死细胞且周围细胞为3个 则死细胞复活
                board[i][j] = '101'
            # else:
            #     board[i][j] = '1' + board[i][j][2] * 2
            # print('board[i][j]={},res={}'.format(board[i][j],res))

        for i in range(len(board)):
            for j in range(len(board[0])):
                chage(i, j, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = int(board[i][j][-1])
        # print(board)


s = Solution()
board=[[0, 1, 0],
      [0, 0, 1],
      [1, 1, 1],
      [0, 0, 0]]


