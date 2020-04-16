#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 16:04
# @Author  : Fhh
# @File    : 29.py
# Good good study,day day up!
# def divide(self, dividend, divisor):
#     i, a, b = 0, abs(dividend), abs(divisor)
#     if a == 0 or a < b:
#         return 0
#
#     while b <= a:
#         b = b << 1
#         i = i + 1
#     else:
#         res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
#         if (dividend ^ divisor) < 0:
#             res = -res
#         return min(res, (1 << 31) - 1)
class Solution:
    def divide(self, dividend, divisor):
        i, a, b = 0, abs(dividend), abs(divisor)
        if a == 0 or a < b:
            return 0
        while b <= a:
            b = b << 1
            i = i + 1
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
            if (dividend ^ divisor) < 0:
                res = -res
            return min(res, (1 << 31) - 1)


s = Solution()
print(s.divide(23, 4))
