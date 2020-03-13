"""给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :param num: int
        :return: bool
        """
        flag = False
        for i in range(1000000):
            if i > num:
                break
            else:
                if i * i == num:
                    flag = True
                    break
        return flag


class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :param num: int
        :return: bool
        """
        flag = False
        if num == 0 or num == 1:
            flag = True
        for i in range(2,int(num/2)+1):
            if i*i==num:
                flag=True
                break
        return flag
s = Solution2()
for i in range(10000):
    if s.isPerfectSquare(i):
        print('{}是完全平方数'.format(i))
