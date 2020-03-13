"""假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        :param n: int
        :return: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        """
        :param n: int
        :return: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            cnt = 3
            while cnt <= n:
                b = a + b
                a = b - a
                cnt += 1
            return b
s = Solution2()
for i in range(1, 20):
    print("爬{}层台阶有{}种方法".format(i, s.climbStairs(i)))
