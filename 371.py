"""
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1"""


class Solution:  # wa for python
    def getSum(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.getSum(a ^ b, (a & b) << 1)


s = Solution()
print(s.getSum(-1, 2))
