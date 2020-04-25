#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 23:48
# @Author  : Fhh
# @File    : 338.py
# Good good study,day day up!
"""给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
示例 1:
输入: 2
输出: [0,1,1]
示例 2:
输入: 5
输出: [0,1,1,2,1,2]
进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num < 0:
            return []
        res = [0]
        k = 1
        m = 2
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                res.append(1)
            else:
                while i >> k > 0:
                    k += 1
                    m *= 2
                res.append(res[i - m] + 1)
        return res


s = Solution()
print(s.countBits(9999999))
