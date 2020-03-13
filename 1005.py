"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

示例 1：

输入：A = [4,2,3], K = 1
输出：5
解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
"""
class Solution:
    def largestSumAfterKNegations(self, A, K) :
        """
        :param A: list[int]
        :param K: int
        :return: int
        """
        while K>0:
            A.sort()
            A[0] = -A[0]
            K -= 1
        cnt=0
        for i in A:
            cnt += i
        return cnt

s = Solution()
a = [-1,-3,4,5,0,1]
b = [3,-1,0,2]
c = [2,-3,-1,5,-4]
print(s.largestSumAfterKNegations(c,2))

