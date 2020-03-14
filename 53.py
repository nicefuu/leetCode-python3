"""给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""


class Solution:
    def maxSubArray(self, nums):
        """

        :param nums:list[int]
        :return: int
        """
        m = max(nums)
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                cnt = 0
                for k in range(i, j + 1):
                    cnt += nums[k]
                if m < cnt:
                    m = cnt
        return m


class Solution2:
    def maxSubArray(self, nums):
        """
        :param nums:list[int]
        :return: int
        """
        res = nums[0]
        fx = 0
        for i in nums:
            if fx > 0:
                fx += i
            else:
                fx = i
            res = max(res, fx)
        return res


s = Solution2()
print((s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])))
# print((s.maxSubArray([-2, 1])))
# print((s.maxSubArray([31])))
# print((s.maxSubArray([-2, -1])))
