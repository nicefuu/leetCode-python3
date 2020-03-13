"""给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return str(bin(n)).count('1') == 1
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        else:
            return n&(n-1)==0
s=Solution2()

for i in range(99999):
    if s.isPowerOfTwo(i):
        print('{}是2的幂次方'.format(i))