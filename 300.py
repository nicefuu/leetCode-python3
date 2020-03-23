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
        n = len(nums)
        if n == 0 or n == 1:  # 数组长度为0或1直接返回长度
            return len(nums)
        else:  # 数组长度大于1
            temp = [1]
            m = 1
            for i in range(1, n):
                temp.append(1)
                j = i - 1
                while j >= 0:
                    if nums[j] < nums[i] and temp[j] + 1 > temp[i]:
                        temp[i] = temp[j] + 1
                    j -= 1
                if m < temp[i]:
                    m = temp[i]
            return m


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 105]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 4]))
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
