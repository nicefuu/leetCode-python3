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

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


class Solution2:
    def permute(self, nums):
        """
        :param nums: list[int]
        :return: list[int]
        """
        ret = []

        def dfs(nums, tmp):
            """
            :param nums:
            :param tmp:
            :return:
            """
            if not nums:
                ret.append(tmp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], tmp.append(nums[i]))

        dfs(nums, [])
        return ret


s = Solution2()
print(s.permute([1, 2, 3, 4]))
