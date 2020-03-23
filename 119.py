"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

"""


class Solution:
    def getRow(self, rowIndex: int):
        """
        :param rowIndex: int
        :return: list[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            res = [1 for _ in range(rowIndex + 1)]
            for i in range(2, rowIndex + 1):
                a = 1
                b = i - 1
                if i & 1 == 0:
                    for j in range(1, int(i / 2) + 1):
                        res[j] = a + b
                        a = b
                        b = res[j + 1]
                    res = res[:int(i / 2) + 1] + res[:int(i / 2)][::-1]
                else:
                    for j in range(1, int((i + 1) / 2)):
                        res[j] = a + b
                        a = b
                        b = res[j + 1]
                    res = res[:int((i + 1) / 2)] + res[:int((i + 1) / 2)][::-1]
            return res


s = Solution()
for i in range(1, 10):
    print(s.getRow(i))
