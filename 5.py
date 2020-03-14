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
        lens = len(s)
        d = [[False for _ in range(lens)] for _ in range(lens)]
        left, right = 0, 0
        m = 1
        for i in range(lens):
            d[i][i] = True
            for k in range(1, lens):
                if i - k >= 0 and i + k < lens:
                    d[i - k][i + k] = d[i - k + 1][i + k - 1] and s[i - k] == s[i + k]
                    if d[i - k][i + k] and m < 2 * k + 1:
                        m = 2 * k + 1
                        left = i - k
                        right = i + k
                else:
                    break
        for i in range(lens - 1):
            if s[i] == s[i + 1]:
                d[i][i + 1] = True
                if m < 2:
                    m = 2
                    left = i
                    right = i + 1
                for k in range(1, lens):
                    if i - k >= 0 and i + 1 + k < lens:
                        d[i - k][i + 1 + k] = d[i - k + 1][i + k] and s[i - k] == s[i + 1 + k]
                        if d[i - k][i + 1 + k] and m < 2 * k + 2:
                            m = 2 * k + 2
                            left = i - k
                            right = i + 1 + k
                    else:
                        break
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
                if m < 2:
                    left = i
                    right = i + 1
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


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1
        start = 0
        for i in range(size):
            dp[i][i] = True
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


class Solution4:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        left, length = 0, 0
        for i in range(1, len(s)):
            A1 = s[i - length - 1:i + 1]
            A2 = s[i - length:i + 1]
            if i - length - 1 >= 0 and A1 == A1[::-1]:
                left = i - length - 1
                length += 2
            if i - length >= 0 and A2 == A2[::-1]:
                left = i - length
                length += 1
        return s[left:length + left]


s = Solution4()
for i in ['cbbd', 'bbbbbb', '', 'kok', 'kacok', "tattarrattat"]:
    print(s.longestPalindrome(i))
