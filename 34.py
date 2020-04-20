#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 12:00
# @Author  : Fhh
# @File    : 34.py
# Good good study,day day up!
"""给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        def binary_search(arr, left, right):
            mid = int(left + right) / 2
            if mid==left:
                return
            else:
                binary_search(arr,left,mid)
                binary_search(arr,mid+1,right)
