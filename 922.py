"""给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""
class Solution:
    def sortArrayByParityII(self, A):
        """
        :param A: list[int]
        :return: list[int]
        """
        even=[]
        odd=[]
        for i in range(len(A)):
            if A[i]%2==0 and i%2==1:
                even.append(i)
            elif A[i]%2==1 and i%2==0:
                odd.append(i)
        for i in range(len(even)):
            A[even[i]] = A[even[i]] + A[odd[i]]
            A[odd[i]] = A[even[i]] - A[odd[i]]
            A[even[i]] = A[even[i]] - A[odd[i]]
        return A
s = Solution()
a = [4,2,5,7]
b = [1,3,4,5,6,8]
print(s.sortArrayByParityII(a))
print(s.sortArrayByParityII(b))
