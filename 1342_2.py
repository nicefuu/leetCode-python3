class Solution:
    def numberOfSteps (self, num: int) -> int:
        b = str(bin(num))[2:]
        print(b)
        return b.count('1')+len(b)-1
s = Solution()
print(s.numberOfSteps(123))