"""如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。
"""
class Solution:
    def isMonotonic(self, A):
        """
        :param A:list[int]
        :return:bool
        """
        b=sorted(A)
        c=b[::-1]
        return A==b or A==c

class Solution2:
    def isMonotonic(self, A):
        """
        :param A:list[int]
        :return:bool
        """
        a=0
        b=0
        if len(A)==1:
            return True
        else:
            for i in range(len(A)-1):
                if A[i] < A[i+1]:
                    a = 1
                if A[i] > A[i+1]:
                    b = 1
            if a==b==1:
                return False
            else:
                return True
s=Solution2()
a=[1,1,2,3,4,5,5]
b=[5,4,3,2,1,0,0]
print(s.isMonotonic(a))
print(s.isMonotonic(b))
