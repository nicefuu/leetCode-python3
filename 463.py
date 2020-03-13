"""给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16
"""


class Solution:
    def islandPerimeter(self, grid) -> int:
        """
        :param grid: list[list[int]]
        :return: int
        """
        newgrid = [[0 for i in range(len(grid[0]) + 2)] for j in range(len(grid) + 2)]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newgrid[i + 1][j + 1] = grid[i][j]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if newgrid[i][j]==1:
                    cnt+=4-(newgrid[i-1][j]+newgrid[i+1][j]+newgrid[i][j-1]+newgrid[i][j+1])
        return cnt


s = Solution()
a = [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
b=[[0,1]]
print(s.islandPerimeter(a))
print(s.islandPerimeter(b))
