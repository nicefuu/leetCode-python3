"""给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
"""


# a-z 97-122
# A-Z 65-90
# 0-9 48-57
class Solution:
    def letterCasePermutation(self, S):
        """
        :param S: str
        :return: list[str]
        """
        ret = []
        st = list(S)
        for i in range(len(st)):
            if 97 <= ord(st[i]) <= 122:
                st[i] = chr(ord(st[i]) - 32)
            elif 65 <= ord(st[i]) <= 90:
                st[i] = chr(ord(st[i]) + 32)
            else:
                continue
            ret.append(''.join(st))
            if 97 <= ord(st[i]) <= 122:
                st[i] = chr(ord(st[i]) - 32)
            elif 65 <= ord(st[i]) <= 90:
                st[i] = chr(ord(st[i]) + 32)
        return ret
s=Solution()
str="3Z4aG"
print(s.letterCasePermutation(str))
