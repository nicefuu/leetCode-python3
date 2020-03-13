"""给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        :param num1: str
        :param num2: str
        :return:str
        """
        # 0-9 48-57
        # n = ord('n') - 48   n is a number
        if len(num1) >= len(num2):
            n1 = num1[::-1]
            n2 = ('0' * (len(num1) - len(num2)) + num2)[::-1]
        else:
            n1 = num2[::-1]
            n2 = ('0' * (len(num2) - len(num1)) + num1)[::-1]
        #print("n1 = " + n1)
        #print("n2 = " + n2)
        i = 0
        p = 0
        r = ''
        while i < len(n1):
            t = ord(n1[i]) - 48 + ord(n2[i]) - 48 + p
            if t < 10:
                r += chr(t + 48)
                p = 0
            else:
                r += chr(t - 10 + 48)
                p = 1
            i += 1
        if p == 1:
            r += '1'
        return r[::-1]


s = Solution()
# s.addStrings('1234', '45')
print(s.addStrings('6', '501'))
