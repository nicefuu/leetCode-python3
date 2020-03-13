"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        :param n:int
        :return: int
        """
        return str(bin(n)).count('1')
s=Solution()
print(s.hammingWeight(55))