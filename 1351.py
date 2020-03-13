class Solution:
    def countNegatives(self, grid):
        cnt=0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]<0:
                    cnt += n-j
                    break
        return cnt
s= Solution()
b =[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(s.countNegatives(b))