"""给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
"""
class Solution:
    def findShortestSubArray(self, nums):
        """
        :param nums: list[int]
        :return: int
        """
        max_int = 0
        max_count = 0
        left_index = 0
        right_index = 0
        len_num = len(nums)
        for i in range(len_num):
            if nums.count(nums[i]) >= max_count:
                max_count = nums.count(i)
                max_int = nums[i]
                right_index = i
        for i in range(len_num):
            if nums[i]==max_int:
                left_index = i
                break
        return right_index-left_index+1
s=Solution()
a = [1,2,2,3,1,4,2]
b = [1, 2, 2, 3, 1]
print(s.findShortestSubArray(b))