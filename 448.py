"""给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :param nums:list[int]
        :return:list[int]
        """
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                if nums[nums[i] - 1] > 0:
                    nums[nums[i] - 1] = -nums[nums[i] - 1]
            elif nums[i] < 0:
                if nums[-nums[i] - 1] > 0:
                    nums[-nums[i] - 1] = -nums[-nums[i] - 1]
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res


class Solution2:
    def findDisappearedNumbers(self, nums):
        """
        :param nums:list[int]
        :return:list[int]
        """
        res = []
        n = len(nums)
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        return res


s = Solution2()
print(s.findDisappearedNumbers([1]))
