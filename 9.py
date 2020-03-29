"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :param x:int
        :return: bool
        """
        return str(x) == str(x)[::-1]


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        """
        :param x:int
        :return: bool
        """
        if x < 0:
            return False
        a = []
        while x > 0:
            a.append(x % 10)
            x = int(x / 10)
        print(a)
        if a == a[::-1]:
            return True
        else:
            return False


s = Solution2()
s.isPalindrome(0)
# for i in range(10000):
#     if s.isPalindrome(i):
#         print(i,end=' ')
