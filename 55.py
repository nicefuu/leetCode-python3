#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 16:58
# @Author  : Fhh
# @File    : 55.py
# Good good study,day day up!
"""给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution1:  # 超时
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if nums[0] + 1 >= len(nums):
            return True
        for i in range(1, nums[0] + 1):
            if self.canJump(nums[i:]):
                return True
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if min(nums) > 0:
            return True



if __name__ == '__main__':
    s = Solution()
    print(s.canJump([1, 2, 3]))
    print(s.canJump([3, 2, 1, 0, 4]))
