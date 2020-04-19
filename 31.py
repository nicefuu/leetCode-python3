#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 22:48
# @Author  : Fhh
# @File    : 31.py
# Good good study,day day up!
"""实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return nums

        def search(arr, x):  # 在arr中找到一个比x大的最小的数，返回他的索引 如果没有，返回-1
            if not arr or len(arr) == 0:
                return -1
            res = None
            for i in range(0, len(arr)):
                if arr[i] > x:
                    if res == None:
                        res = i
                    else:
                        res = i if arr[res] > arr[i] else res
            return res

        key = len(nums) - 2
        while key >= 0:
            min = search(nums[key + 1:], nums[key])
            if min != None:
                nums[key + min + 1], nums[key] = nums[key], nums[key + min + 1]
                nums[:] = nums[:key+1] + sorted(nums[key+1:])
                return
            else:
                key -= 1
        nums.sort()
        return


s = Solution()
a = [1,3,2]
s.nextPermutation(a)
print(a)
