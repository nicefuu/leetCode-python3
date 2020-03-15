"""给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""


class Solution:
    def lengthOfLIS(self, nums):
        """

        :param nums: list[int]
        :return: int
        """
        lenn = len(nums)
        if lenn <= 1:
            return lenn
        m = 1
        for i in range(lenn - 1):
            templen = 1
            head = nums[i]
            for j in range(i + 1, lenn):
                if nums[j] > head:
                    templen += 1
                    head = nums[j]
            if templen > m:
                m = templen
        return m


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18,105]))
print(s.lengthOfLIS([10,9,2,5,3,4]))
