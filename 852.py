"""我们把符合下列属性的数组 A 称作山脉：
A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
"""
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :param A: list[int]
        :return: int
        """
        r=0
        for i in range(1,len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                r=i
        return r
s=Solution()
a=[0,2,1,0]
b=[0,1,3,4,5,6,5,4,2,1,0]
print(s.peakIndexInMountainArray(a))
print(s.peakIndexInMountainArray(b))

