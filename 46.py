"""给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
通过次数
"""


class Solution:
    def permute(self, nums):
        """
        :param nums: list[int]
        :return: list[int]
        """
        res = []
        def back(temp, nums):
            if not nums:
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    back(temp +[nums[i]], nums[:i] + nums[i + 1:])
        back([], nums)
        return res


s = Solution()
print(s.permute([1, 2, 3, 4]))
