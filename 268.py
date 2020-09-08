#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 14:32
# @Author  : Fhh
# @File    : 268.py
# @Software: PyCharm
# good good study,day day up!
"""
给定一个包含 0, 1, 2, ..., n中n个数的序列，找出 0 .. n中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        for i in range(len(nums)):
            sum += nums[i] - n + i
        return abs(sum)


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
