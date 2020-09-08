#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 15:50
# @Author  : Fhh
# @File    : 204.py
# Good good study,day day up!
"""统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。"""


class Solution:  # 超时
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        for i in range(2, n):
            if i & 1 == 1:
                isprime = True
                for p in primes:
                    if p > int(n ** 0.5) + 1:
                        break
                    else:
                        if i % p == 0:
                            isprime = False
                            break
                if isprime:
                    primes.append(i)
        return len(primes)


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True for _ in range(n)]
        for i in range(2, n):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return primes[2:].count(True)


s = Solution2()
print(s.countPrimes(1500000))
