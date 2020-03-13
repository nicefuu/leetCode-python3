"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
"""
class Solution:
    def sortArrayByParity(self, A):
        """
        :param A: list[int]
        :return: list[int]
        """
        r=[]
        for i in A:
            if i%2==0:
                r.append(i)
        for i in A:
            if i%2!=0:
                r.append(i)
        return r
s=Solution()
a=[3,1,2,4]
print(s.sortArrayByParity(a))