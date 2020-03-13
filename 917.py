"""给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
"""


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :param S: str
        :return: str
        """
        a = list(S)
        temp = []
        for i in range(len(a)):
            if a[i].isalpha():
                temp.append(a[i])
        temp = temp[::-1]
        j = 0
        for i in range(len(a)):
            if a[i].isalpha():
                a[i] = temp[j]
                j += 1
        return (''.join(a))


s = Solution()
a = "a-bC-dEf-ghIj"
b = "Test1ng-Leet=code-Q!"
print(s.reverseOnlyLetters(a))
print(s.reverseOnlyLetters(b))
