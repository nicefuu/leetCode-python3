"""泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
"""
class Solution:
    def tribonacci(self, n):
        """
        :param n: int
        :return: int
        """
        f = [0, 1, 1]
        t = 2
        while t < n:
            f.append(f[len(f) - 1] + f[len(f) - 2] + f[len(f) - 3])
            t += 1
        return f[n]

s=Solution()
x=10
print(s.tribonacci(10))