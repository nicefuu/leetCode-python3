"""在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。

示例 1：
输入：[1,2,3,3]
输出：3
"""
class Solution:
    def repeatedNTimes(self, A):
        """
        :param A:
        :return:
        """
        r=0
        for i in A:
            if A.count(i)>1:
                r=i
        return r

class Solution2:
    def repeatedNTimes(self, A):
        """
        :param A:
        :return:
        """
        r=0
        for i in range(len(A)-2):
            if A[i]==A[i+1] or A[i]==A[i+2]:
                r=A[i]
                break
            if len(A) == 4:
                if A[0]==A[3] or A[2]== A[3]:
                    r=A[3]

        return r
s=Solution2()
a=[1,1,2,3,4,5,6,1]
b=[5,1,5,2,5,3,5,4]
c=[1,2,3,3]
e = [1,2,3,4,5,5,5,5]
print(s.repeatedNTimes(c))