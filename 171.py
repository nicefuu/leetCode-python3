#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 15:09
# @Author  : Fhh
# @File    : 171.py
# Good good study,day day up!
"""

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
A-Z 65-90
"""


class Solution(object):

    def titleToNumber(self, s):
        # 26进制转10进制
        ans = 0
        for x in s:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans
