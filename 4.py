#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 17:16
# @Author  : Fhh
# @File    : 4.py
# Good good study,day day up!

"""给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) & 1 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 + 1]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = len(nums1), len(nums2)
        if x * y == 0:
            tmp = nums1 if y == 0 else nums2
            if len(tmp) & 1 == 0:
                return (tmp[len(tmp) - 1 >> 1] + tmp[(len(tmp) >> 1)]) / 2
            else:
                return tmp[len(tmp) >> 1]
        else:
            i, j = 0, 0
            keya = nums1[0]
            keyb = keya
            flag = (x + y) >> 1
            while 1:
                if i + j == flag + 1:
                    if (x + y) & 1 == 1:
                        return keya
                    else:
                        return (keya + keyb) / 2
                if i == x:
                    keyb = keya
                    keya = nums2[j]
                    j += 1
                    continue
                elif j == y:
                    keyb = keya
                    keya = nums1[i]
                    i += 1
                    continue
                else:
                    if nums2[j] < nums1[i]:
                        keyb = keya
                        keya = nums2[j]
                        j += 1
                    else:
                        keyb = keya
                        keya = nums1[i]
                        i += 1


s = Solution2()
print(s.findMedianSortedArrays([], [2,3]))
