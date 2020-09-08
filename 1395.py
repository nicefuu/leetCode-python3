#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 14:02
# @Author  : Fhh
# @File    : 1395.py
# Good good study,day day up!
"""n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

每 3 个士兵可以组成一个作战单位，分组规则如下：

从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。

 

示例 1：

输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
示例 2：

输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。
示例 3：

输入：rating = [1,2,3,4]
输出：4
 

提示：

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-teams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not rating or len(rating) < 3:
            return 0
        res = []
        def f(tmp,isup,rating):
            if len(tmp)==3:
                res.append(tmp)
                return
            if len(rating)==0:
                return
            for i in range(len(rating)):
                if not tmp:
                    f([rating[i]],isup,rating[i+1:])
                else:
                    if isup and rating[i]>tmp[-1]:
                        f(tmp+[rating[i]],isup,rating[i+1:])
                    elif not isup and rating[i]<tmp[-1]:
                        f(tmp+[rating[i]],isup,rating[i+1:])
            return
        f([],True,rating)
        f([],False,rating)
        return len(res)


s = Solution()
print(s.numTeams([2, 5, 3, 4, 1]))
