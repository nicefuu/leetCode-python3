#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 12:05
# @Author  : Fhh
# @File    : 56.py
# Good good study,day day up!
"""给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间
"""


# q=[[1,5],[0,7],[4,8]]按第二列排序
# q=sorted(q,key=lambda q:q[1])
# print(q)
class Solution:
    def merge(self, intervals):
        """
        :param intervals: list[list[int]]
        :return: list[list[int]]
        """
        if not intervals or len(intervals) <= 1:
            return intervals
        res = []
        base = []
        intervals=sorted(intervals)
        for index in range(0, len(intervals)):
            if index == 0:
                base = intervals[index]
            else:
                if intervals[index][0] > base[1]:
                    res.append(base)
                    base = intervals[index]
                elif intervals[index][1] > base[1]:
                    base = [base[0], intervals[index][1]]
            if index==len(intervals)-1:
                res.append(base)
        return res


s = Solution()
a = [[1, 3], [2, 6], [8, 10], [15, 18]]
b=[[1,4],[4,5]]
c=[[1,4],[0,4]]
print(s.merge(a))
print(s.merge(b))
print(s.merge(c))
