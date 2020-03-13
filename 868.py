"""给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。 

如果没有两个连续的 1，返回 0 。
示例 1：

输入：22
输出：2
解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。"""


class Solution:
    def binaryGap(self, N: int) -> int:
        """
        :param N: int
        :return: int
        """
        s = str(bin(N)[2:])
        m = 0
        cnt = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == '1' and s[i + 1] == '1':
                cnt += 1
            else:
                if cnt > m:
                    m = cnt
                cnt = 0
            i += 1
        if m == 0 and cnt == 0:
            return 0
        elif m > cnt:
            return m + 1
        else:
            return cnt + 1


class Solution2:
    def binaryGap(self, N: int) -> int:
        """
        :param N: int
        :return: int
        """
        s = str(bin(N))
        m = 0
        cnt = 0
        for i in range(2, len(s) - 1):
            if s[i] == '1' and s[i + 1] == '1':
                cnt += 1
                if cnt > m:
                    m = cnt
        if m == 0:
            return m
        else:
            return m + 1


# Solution&Solution2 都是计算连续1的个数
class Solution3:
    def binaryGap(self, N: int) -> int:
        """
        :param N: int
        :return: int
        """
        b = str(bin(N))
        m = 0
        left = 0
        right = 0
        for i in range(2, len(b)):
            if b[i] == '1':
                if left == right == 0:
                    right = i
                else:
                    left = right
                    right = i
                    if right - left > m:
                        m = right - left
        return m

sol = Solution3()
for i in range(50):
    print('{0}的二进制为{1}，连1最远距离为{2}'.format(i, str(bin(i))[2:], sol.binaryGap(i)))
