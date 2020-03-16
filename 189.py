"""给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
"""


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        :param nums: list[int]
        :param k: int
        :return: None
        """
        n = k % len(nums)
        if n > 0 and len(nums) > 1:
            sub = nums[:len(nums) - n]
            nums = nums[-n:]
            for i in range(len(sub)):
                nums.append(sub[i])
        print(nums)


class Solution2:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        :param nums: list[int]
        :param k: int
        :return: None
        """
        k = k % len(nums)
        for _ in range(len(nums)-k):
            nums.append(nums[0])
            del nums[0]
        print(nums)

s = Solution2()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
