class Solution:
    def intersection(self, nums1, nums2) :
        num =[]
        for i in nums1:
            if i in nums2 and i not in num:
                num.append(i)
        return num

class Solution2:
    def intersection(self, nums1, nums2) :
        return list(set(nums1) & set(nums2))
s= Solution2()
a = [1,2,2,1,4,5,6,7,7777,8]
b = [1,2,2,7,9,8]
print(s.intersection(a,b))
print(list(set(a)&set(b)))