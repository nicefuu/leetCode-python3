"""给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        :param num: list[int]
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums) + 1):
            if nums[-i] == 0 and i != 1:
                j = i
                while j != 1:
                    t = nums[-j]
                    nums[-j] = nums[-j + 1]
                    nums[-j + 1] = t
                    j -= 1


class Solution2:
    def moveZeroes(self, nums) -> None:
        """
        :param num: list[int]
        Do not return anything, modify nums in-place instead.
        """



ss = Solution()
a = [0, 0, 0, 0, 0]
ss.moveZeroes(a)
print(a)
