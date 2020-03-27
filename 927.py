"""给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：

A[0], A[1], ..., A[i] 组成第一部分；
A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。
注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，
而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。

示例 1：
输入：[1,0,1,0,1]
输出：[0,3]
示例 2：
输出：[1,1,0,1,1]
输出：[-1,-1]
提示：
3 <= A.length <= 30000
A[i] == 0 或 A[i] == 1
"""


class Solution:
    def threeEqualParts(self, A):
        """
        :param A:list[int]
        :return: list[int]
        """
        if len(A) < 3:
            return [-1, -1]
        for k in range(len(A)):
            if A[k] == 0:
                A[k] = '0'
            else:
                A[k] = '1'
        all_ones = A.count('1')
        if all_ones == 0:
            return [0, 2]
        if all_ones % 3 != 0:
            return [-1, -1]
        ones = int(all_ones / 3)
        cnt = 0
        i, j = -1, -1
        for index in range(len(A)):
            if A[index] == '1':
                cnt += 1
            if cnt == ones:
                if i == -1:
                    i = index
            if cnt == ones * 2:
                j = index
                break
        zeros_after_ones = 1
        while A[i + zeros_after_ones] == '0':
            if j + zeros_after_ones < len(A):
                if A[j + zeros_after_ones] == '0':
                    zeros_after_ones += 1
                else:
                    break
            else:
                break
        zeros_after_ones -= 1
        zeros_in_the_end = 0
        while zeros_in_the_end < len(A):
            if A[-zeros_in_the_end - 1] == '0':
                zeros_in_the_end += 1
            else:
                break
        if zeros_in_the_end > zeros_after_ones:
            return [-1, -1]
        else:
            x1 = int(''.join(A[:i + 1]))
            x2 = int(''.join(A[i + 1:j + 1]))
            x3 = int(''.join(A[j + 1:len(A) - zeros_in_the_end]))
            if x1 == x2 == x3:
                return [i + zeros_in_the_end, j + zeros_in_the_end + 1]
            else:
                return [-1, -1]


s = Solution()
print(s.threeEqualParts([1, 0, 1, 0, 1]))
print(s.threeEqualParts([1, 0, 1, 0]))
print(s.threeEqualParts([1, 1, 0, 1, 1]))
print(s.threeEqualParts([0, 0, 0, 0, 0]))
print(s.threeEqualParts(
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
     1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]))
