class Solution:
    def printNumbers(self, n) :
        num =[]
        for i in range(1,10**n):
            num.append(i)
        return num
s= Solution()
print(s.printNumbers(2))