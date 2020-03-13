class Solution:
    def reverseLeftWords(self, s, n):
        s2 = s[n:]
        sr = s[:n][::-1]
        return s2+sr
s = Solution()

print(s.reverseLeftWords("asdfgh",3))