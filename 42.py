#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 16:36
# @Author  : Fhh
# @File    : 42.py
# Good good study,day day up!
"""给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:  # 暴力(超时)
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        res = 0
        for i in range(1, len(height) - 1):
            left = 0
            right = 0
            x = i - 1
            while x >= 0:
                left = height[x] if height[x] > left else left
                x -= 1
            x = i + 1
            while x < len(height):
                right = height[x] if height[x] > right else right
                x += 1
            res += max(min(left, right) - height[i], 0)
        return res


class Solution2:  #
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        left = height[0]
        right = max(height[1:])
        res = 0
        for i in range(1, len(height) - 1):
            res += max(min(left, right) - height[i], 0)
            left = height[i] if height[i] > left else left
            right = max(height[i + 1:]) if height[i] >= right else right
        return res


s = Solution2()
print(s.trap([4,2,3]))
