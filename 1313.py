class Solution:
    def decompressRLElist(self, nums) :
        index = nums[::2]
        val = nums[1::2]
        rt=[]
        for i in range(len(index)):
            for j in range(index[i]):
                rt.append(val[i])
        return rt
s = Solution()
str =[1,2,3,4]
print(s.decompressRLElist(str))
