"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:假设字符串的长度不会超过 1010。
示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        return len(s) - max(0, sum([s.count(i) % 2 for i in set(s)]) - 1)


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        count = 0
        for j in d:
            count += d[j] // 2 * 2
            if d[j] % 2 == 1 and count % 2 == 0:
                count += 1
        return count


class Solution3:
    def longestPalindrome(self, s: str) -> int:
        """
        :param s: str
        :return: int
        """
        cnt = 0
        sset = set(s)
        for i in sset:
            cnt += int(s.count(i) // 2) *2
        for i in sset:
            if s.count(i) % 2 == 1:
                cnt +=1
                break
        return cnt


s = Solution3()
a = 'a'
print(s.longestPalindrome(a))
