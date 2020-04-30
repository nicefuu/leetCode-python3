#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 14:32
# @Author  : Fhh
# @File    : 77.py
# Good good study,day day up!
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        arrn=[x for x in range(1,n+1)]
        def func(tmp,k,arr):
            if len(tmp)==k:
                res.append(tmp)
                return
            for i in range(len(arr)):
                if not tmp or (len(tmp)>0 and arr[i]>tmp[-1]):
                    func(tmp+[arr[i]],k,arr[:i]+arr[i+1:])
        func([],k,arrn)
        return res

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k>n or k<0:
            return []
        if k==1:
            return [[x] for x in range(1,n+1)]
        if k==n:
            return [[x for x in range(1,n+1)]]
        res=self.combine(n-1,k)
        for item in self.combine(n-1,k-1):
            item.append(n)
            res.append(item)
        return res

