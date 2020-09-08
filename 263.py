#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 14:12
# @Author  : Fhh
# @File    : 263.py
# @Software: PyCharm
# good good study,day day up!
"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数2, 3, 5的正整数。

示例1:

输入: 6
输出: true
解释: 6 = 2 ×3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 ×2
示例3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数7。
说明：

1是丑数。
输入不会超过 32 位有符号整数的范围:[−231, 231− 1]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        if num==0:
            return False
        while (num % 2) == 0:
            num //= 2
        while (num % 3) == 0:
            num //= 3
        while (num % 5) == 0:
            num //= 5
        return num == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
