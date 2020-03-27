"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2)."""
import time


class Solution:  # 超时
    def threeSumClosest(self, nums, target: int) -> int:
        """
        :param nums:list[int]
        :param target: int
        :return: int
        """
        if len(nums) < 3:
            return 0
        res = abs(nums[0] + nums[1] + nums[2] - target)
        a, b, c = nums[0], nums[1], nums[2]
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if abs(nums[i] + nums[j] + nums[k] - target) < res:
                        res = abs(nums[i] + nums[j] + nums[k] - target)
                        a, b, c = nums[i], nums[j], nums[k]
        return a + b + c


class Solution2:
    def threeSumClosest(self, nums, target: int) -> int:
        """
        :param nums:list[int]
        :param target: int
        :return: int
        """
        if len(nums) == 0:
            return 0
        cnt = 0
        if len(nums) <= 3:
            for i in range(len(nums)):
                cnt += nums[i]
            return cnt
        nums.sort()
        delta = 0
        while 1:
            for start in range(len(nums) - 2):
                left = start + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] + nums[start] == target + delta:
                        return nums[left] + nums[right] + nums[start]
                    elif nums[left] + nums[right] + nums[start] > target + delta:
                        right -= 1
                    else:
                        left += 1
            for start in range(len(nums) - 2):
                left = start + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] + nums[start] == target - delta:
                        return nums[left] + nums[right] + nums[start]
                    elif nums[left] + nums[right] + nums[start] > target - delta:
                        right -= 1
                    else:
                        left += 1
            delta += 1


start_time = time.time()
s = Solution2()
for _ in range(5):
    print(s.threeSumClosest(
        nums=[36, 38, 95, -89, -86, -19, 63, -8, 12, 90, 15, -84, 48, 50, 88, 88, -29, -2, 99, -97, 60, 88, 30, 64, -28,
              -87, 2, 78, 87, 97, 77, 63, 77, 62, 89, 57, 39, -36, 39, -43, 86, 76, 32, -71, -46, 58, 18, -27, 52, -68,
              -79,
              -54, 0, 18, -88, 72, -57, 95, -66, 73, -99, 33, -16, 43, 81, 40, 0, -8, -15, 6, 87, -43, 92, -64, 68, 1,
              -32,
              15, -60, -49, 35, 31, 49, -70, 65, 0, -87, 27, 12, 2, -94, 79, 4, 41, 19, -37, -79, -22, 7, -25, -67, -56,
              34,
              -64, -7, -58, 2, 26, 98, 2, 23, 2, 7, 62, 49, -18, 44, -1, 91, 56, 64, -98, -84, 38, 23, 63, -80, 14, 56,
              -100, -62, 19, 24, -16, 18, -78, -52, 47, 99, 82, -91, -34, 76, 89, -56, -35, -72, -90, 41, 43, -43, 6,
              -95,
              -63, -70, -81, -55, -63, -28, -61, -72, 68, -50, 72, -28, 83, 67, 99, 41, 54, 73, -4, 14, -91, 51, 93, 46,
              32,
              -49, 87, -84, -13, 57, 12, 74, 42, 33, 39, -79, -56, -46, -53, -74, -88, 55, -65, -75, -89, -56, 97, 100,
              7,
              84, 79, 8, 24, 48, -46, -95, 76, 73, -87, 85, 45, -8, -69], target=171), end=" ")

end_time = time.time()
print("程序运行时间={:.5f}s".format((end_time - start_time) / 5))
print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0, 0, 0, 1], 1))
