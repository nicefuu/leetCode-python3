class Solution:
    def sumZero(self, n):
        list = []
        if n == 1:
            return [0]
        return range(-n-1,n,2)

s =Solution()
print(s.sumZero(8).reverse())
