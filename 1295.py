
class Solution:
    def findNumbers(self, nums):
        if not nums:
            return 0
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
class Solution2:
    def findNumbers(self, nums):
        if not nums:
            return 0
        count = 0
        for i in nums:
            if((i >= 10 and i <= 99) or (i >= 1000 and i <= 9999) or (i >= 100000 and i <= 999999)):
                count += 1
        return count
x= Solution2()
list1 =[1,22,33,44,1123,12312,2,3]
print(x.findNumbers(list1))