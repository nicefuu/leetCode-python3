#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 16:46
# @Author  : Fhh
# @File    : 219.py
# Good good study,day day up!
"""给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

 

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums)<2:#数组长度小于2则不存在
            return False
        d=dict()
        for index,num in enumerate(nums):
            # 如num在d里且距离是否小于等于k，返回True，其他情况d[num]=index
            if num in d and index-d[num]<=k:
                return True
            d[num]=index
        return False
s=Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))