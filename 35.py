"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
"""


class Solution:
    def searchInsert(self, nums, target):
        """

        :param nums: list[int]
        :param target: int
        :return: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        else:
            index=0
            while target>nums[index]:
                index+=1
                if index==len(nums):
                    return len(nums)
            return index

s = Solution()
print(s.searchInsert([0,1,2], -2))
