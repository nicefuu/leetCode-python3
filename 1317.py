"""「无零整数」是十进制表示中 不含任何 0 的正整数。

给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足：

A 和 B 都是无零整数
A + B = n
题目数据保证至少有一个有效的解决方案。

如果存在多个有效解决方案，你可以返回其中任意一个。

 

示例 1：

输入：n = 2
输出：[1,1]
解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。
示例 2：

输入：n = 11
输出：[2,9]
示例 3：

输入：n = 10000
输出：[1,9999]
"""


class Solution:
    def getNoZeroIntegers(self, n: int):
        """
        :param n: int
        :return: list[int]
        """
        A, B = '', ''
        if n <= 10:
            A = 1
            B = n - 1
        else:
            ls = list(str(n))
            for i in range(len(ls)):
                ls[i] = int(ls[i])
            for i in range(1, len(ls)):
                if ls[-i] < 2:
                    ls[-i] = ls[-i] + 10
                    ls[-i - 1] = ls[-i - 1] - 1
            for i in range(0, len(ls)):
                if ls[i] == 0:
                    continue
                elif ls[i] == 1:
                    A += '1'
                elif ls[i] == 11:
                    A += '2'
                    B += '9'
                else:
                    A += '1'
                    B += str(ls[i] - 1)
        return [int(A), int(B)]


class Solution2:
    def getNoZeroIntegers(self, n: int):
        """
        :param n: int
        :return: list[int]
        """
        A=0
        B=0
        for x in range(1, n):
            if str(x).count('0') == 0 and str(n - x).count('0') == 0:
                A=x
                B=n-x
                break
        return [A, B]


s = Solution2()
n = 4
s.getNoZeroIntegers(n)
print(s.getNoZeroIntegers(n))
cnt = 0
for i in range(2,10000):
    if s.getNoZeroIntegers(i)[0] + s.getNoZeroIntegers(i)[1] != i:
        print(s.getNoZeroIntegers(i), end='')
        print('={}'.format(i))
        cnt += 1
if cnt==0:
    print("ok")
