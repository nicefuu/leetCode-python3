"""给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。"""
class Solution:
    def transpose(self, A):
        """
        :param A: list[list[int]]
        :return: list[list[int]]
        """
        a=list(zip(*A))
        for i in range(len(a)):
             a[i]=list(a[i])
        return a
s=Solution()
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.transpose(a))