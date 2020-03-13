class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        :param n:int
        :return: bool
        """
        if n == 1 or n == 2:
            return True
        else:
            return str(bin(n)[2:]) == '10' + str(bin(n >> 2))[2:]


s = Solution()
for n in range(100000):
    if s.hasAlternatingBits(n):
        print('{}是交替位二进制数'.format(n))
        print(bin(n)[2:])
