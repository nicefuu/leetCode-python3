"""给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:

输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)
"""
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :param L: int
        :param R: int
        :return: int
        """
        b = 0
        cnt = 0
        for i in range(L,R+1):
            b = str(bin(i))[2:]
            if self.isprime(b.count('1')):
                cnt += 1
        return cnt

    def isprime(self,n):
        flag = True
        if n==1 or n==0:
            flag=False
        else:
            for i in range(2,n):
                if n%i==0:
                    flag = False
                    break
        return flag
class Solution2:
    def countPrimeSetBits(self, L, R):
        """
        :param L: int
        :param R: int
        :return: int
        """
        temp =[2,3,5,7,11,13,17,19,23,29,31]
        cnt=0
        for i in range(L,R+1):
            if str(bin(i)).count('1') in temp:
                cnt += 1
        return cnt

s= Solution2()
print(s.countPrimeSetBits(10,15))


