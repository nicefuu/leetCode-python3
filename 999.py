"""
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，
直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
返回车能够在一次移动中捕获到的卒的数量。
 """


class Solution:
    def numRookCaptures(self, board) -> int:
        """
        :param board:list[list[str]]
        :return: int
        """
        r = []
        findrook = False
        for i in range(8):
            if findrook:
                break
            for j in range(8):
                if board[i][j] == 'R':
                    findrook = True
                    r = [i, j]
                    break
        cnt = 0
        x, y = r[0], r[1]
        while x < 7:
            if board[x + 1][r[1]] == 'p':
                cnt += 1
                break
            elif board[x + 1][r[1]] == 'B':
                break
            x += 1
        while y < 7:
            if board[r[0]][y + 1] == 'p':
                cnt += 1
                break
            elif board[r[0]][y + 1] == 'B':
                break
            y += 1
        x, y = r[0], r[1]
        while x > 0:
            if board[x - 1][r[1]] == 'p':
                cnt += 1
                break
            elif board[x - 1][r[1]] == 'B':
                break
            x -= 1
        while y > 0:
            if board[r[0]][y - 1] == 'p':
                cnt += 1
                break
            elif board[r[0]][y - 1] == 'B':
                break
            y -= 1
        return cnt
s=Solution()
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","R",".",".",".","p"],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]))
print(s.numRookCaptures([["R",".",".",".",".",".",".","."],
                         [".","p","p","p","p","p",".","."],
                         [".","p","p","B","p","p",".","."],
                         [".","p","B",".","B","p",".","."],
                         [".","p","p","B","p","p",".","."],
                         [".","p","p","p","p","p",".","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]))
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         ["p","p",".","R",".","p","B","."],
                         [".",".",".",".",".",".",".","."],
                         [".",".",".","B",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]))
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".","p","p",".",".",".","."],
                         [".","p","p","R",".","p",".","p"],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".","p",".","."],
                         [".",".",".","p",".",".",".","."],
                         [".",".",".",".",".",".",".","."]]))