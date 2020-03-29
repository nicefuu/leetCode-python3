"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :param s:str
        :return: int
        """
        if not s:
            return 0
        if len(s) < 2:
            return len(s)
        left = 0
        right = 1
        m = 1
        while right < len(s):
            if len(s[left:right + 1]) == len(set(s[left:right + 1])):
                if right + 1 - left > m:
                    m = right + 1 - left
                right += 1
            else:
                while s[left] != s[right]:
                    left += 1
                left += 1
                # right=left+1
        return m

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        if len(s) != 0:
            Subs = s[0]
        else: return 0
        for i in range(len(s)):
            flag = Subs.find(s[i])
            Subs = Subs + s[i] if (flag == -1) else Subs[flag + 1:] + s[i]
            Max = len(Subs) if len(Subs) > Max else Max
        return Max


s = Solution()
print(s.lengthOfLongestSubstring("dvedffghijkkk"))
