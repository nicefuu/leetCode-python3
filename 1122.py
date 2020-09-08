#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 12:32
# @Author  : Fhh
# @File    : 1122.py
# Good good study,day day up!
"""给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

 

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 

提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        for index, num in enumerate(arr2):  # 创建字典储存arr2中数字以及索引
            d[num] = index
        tmp = []
        othernum = []  # 用来存arr1中未在arr2中出现的数字
        for i in arr1:
            if i in d:  # 如果arr1中的元素在arr2中即在字典中出现则存入tmp（第一列为改数字，第二列为数字的索引）否则存入othernum
                tmp.append([i, d[i]])
            else:
                othernum.append(i)
        tmp = sorted(tmp, key=lambda x: x[1])  # 对tmp数组按第二列即在arr2中的索引排序
        return list(list(zip(*tmp))[0]) + sorted(othernum)


class Solution2:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tmp = [0 for _ in range(1001)]
        for i in arr1:
            tmp[i] += 1
        res = []
        for i in arr2:
            res += [i] * tmp[i]
            tmp[i] = 0
        for i in range(1001):
            if tmp[i] != 0:
                res += [i] * tmp[i]
        return res


s = Solution2()
print(s.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
