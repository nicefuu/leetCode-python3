#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 13:53
# @Author  : Fhh
# @File    : 1013.py
# Good good study,day day up!
"""给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

 

示例 1：

输入：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
示例 2：

输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
示例 3：

输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

提示：

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


# from functools import reduce


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if not A or len(A) < 3 or sum(A) % 3 != 0:
            return False
        s = sum(A)
        left, right = 0, len(A) - 1
        while left < right - 1:
            sum_l = sum(A[:left + 1])
            sum_r = sum(A[right:])
            if sum_l == s / 3 and sum_r == s / 3:
                return True
            if sum_l != s / 3:
                left += 1
            if sum_r != s / 3:
                right -= 1

        return False


s = Solution()
print(s.canThreePartsEqualSum([1, -1, 1, -1]))
