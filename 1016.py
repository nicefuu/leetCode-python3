#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 15:22
# @Author  : Fhh
# @File    : 1016.py
# Good good study,day day up!
"""给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的子串，就返回 true，否则返回 false。

 

示例 1：

输入：S = "0110", N = 3
输出：true
示例 2：

输入：S = "0110", N = 4
输出：false
 

提示：

1 <= S.length <= 1000
1 <= N <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N, 0, -1):
            if bin(i)[2:] not in S:
                print(bin(i))
                return False
        return True


s = Solution()
print(s.queryString('1', 1))
