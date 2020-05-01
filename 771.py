#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 17:50
# @Author  : Fhh
# @File    : 771.py
# Good good study,day day up!
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        jews = dict()
        for jew in J:
            jews[jew] = 0
        res = 0
        for jew in S:
            if jew in jews:
                res += 1
        return res


class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from functools import reduce

        return reduce(lambda x, y: x + y, map(lambda x: x in J, S))


s = Solution2()
print(s.numJewelsInStones('ASa', 'qwewqasAAA'))
