class Solution:
    def subtractProductAndSum(self, n):
        s = str(n)
        m = 1
        for x in range(len(s)):
            m *= int(s[x])
        print(m)
        p = 0
        for y in range(len(s)):
            p += int(s[y])
        print(p)
        return m-p
solution = Solution()
t = 2345
print(solution.subtractProductAndSum(t))