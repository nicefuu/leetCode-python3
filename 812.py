"""给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
hint：三角形面积用行列式计算(x1,y1),(x2,y2),(x3,y3)
  |x1  y1  1|
S=|x2  y2  1|
  |x3  y3  1|
"""


class Solution:
    def largestTriangleArea(self, points) -> float:
        """
        :param points:list[list[int]]
        :return: float
        """
        m = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if i < j < k:
                        t = abs((points[i][0] * points[j][1] + points[i][1] * points[k][0]
                             + points[j][0] * points[k][1] - points[i][0] * points[k][1]
                             - points[i][1] * points[j][0] - points[j][1] * points[k][0]) / 2)
                        if t > m:
                            m = t
        return m


s = Solution()
a = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
b=[[4,6],[6,5],[3,1]]
#print(s.largestTriangleArea(a))
print(s.largestTriangleArea(b))
