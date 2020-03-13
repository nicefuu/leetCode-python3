"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows) :
        """

        :param numRows: int
        :return:list[list[int]]
        """
        nrow = []
        if n==0:
            return []
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return[[1],[1,1]]
        else:
            lastrow = self.generate(numRows - 1)[numRows - 2]
            for i in range(numRows):
                if i == 0 or i == numRows-1:
                    nrow.append(1)
                else:
                    nrow.append(lastrow[i-1]+lastrow[i])
        gn = self.generate(numRows-1)
        gn.append(nrow)
        return gn

class Solution2:
    def generate(self, numRows) :
        """

        :param numRows: int
        :return:list[list[int]]
        """
        yh=[]
        if numRows >= 1:
            yh.append([1])
        if numRows >= 2:
            yh.append([1,1])
        if numRows >= 3:
            nrow=[]
            for i in range(2,numRows):
                for j in range(i+1):
                    if j==0 or j==i:
                        nrow.append(1)
                    else:
                        nrow.append(yh[i-1][j-1]+yh[i-1][j])
                yh.append(nrow)
                nrow=[]
        return yh


s=Solution2()
n=7
print(s.generate(n))
