"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        :param s: str
        :return: str
        """
        d = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            d[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                d[i][i + 1] = True
        max = 1
        left = 0
        right = 0
        for i in range(len(s) - 2, -1, -1):
            for j in range(1, len(s)):
                if i != j and j != i + 1:
                    d[i][j] = (d[i + 1][j - 1] and s[i] == s[j])
                if d[i][j] and max < j - i + 1:
                    left = i
                    right = j
                    max = j - i + 1
        if right == len(s) - 1:
            return s[left:]
        else:
            return s[left:right + 1]


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """
        :param s: str
        :return: str
        """
        left = 0
        right = 0
        m = 1
        for i in range(len(s) - 1):
            c1 = 1
            for j in range(1, len(s)):
                if i + j < len(s) and i - j >= 0:
                    if s[i - j] == s[i + j]:
                        c1 += 2
                    else:
                        break
                    if m < c1:
                        m = c1
                        left = i - j
                        right = i + j
            if s[i] == s[i + 1]:
                c2 = 2
                if m<2:
                    left=i
                    right=i+1
                for j in range(1, len(s)):
                    if i + 1 + j < len(s) and i - j >= 0:
                        if s[i - j] == s[i + 1 + j]:
                            c2 += 2
                            if m < c2:
                                m = c2
                                left = i - j
                                right = i + j + 1
                        else:
                            break

        if right == len(s) - 1:
            return s[left:]
        else:
            return s[left:right + 1]


s = Solution2()
for i in ['cccccc','ccc','cbbd','abcda','qweeewq']:
    print(s.longestPalindrome(i))
