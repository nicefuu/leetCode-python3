"""给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        :param num: int
        :return: bool
        """
        if num<=0:
            return False
        elif num == 1:
            return True
        else:
            if str(bin(num)).count('0') % 2 == 1 and str(bin(num)).count('1') == 1:
                return True
            else:
                return False


s = Solution()
for i in range(2 ** 32):
    if s.isPowerOfFour(i):
        print('{}是4的整数幂'.format(i))
        print(bin(i))
