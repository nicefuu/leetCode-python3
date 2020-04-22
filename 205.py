#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 23:10
# @Author  : Fhh
# @File    : 205.py
# Good good study,day day up!
"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = {}
        dictt = {}

        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = t[i]
            elif dicts[s[i]] != t[i]:
                return False
            if t[i] not in dictt:
                dictt[t[i]] = s[i]
            elif dictt[t[i]] != s[i]:
                return False
            if len(dicts) != len(dictt):
                return False
        return True
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = [t[i]]
                if len(dict) != len(set(dict.values())):
                    return False
            elif dict[s[i]] != t[i]:
                return False
        return True
s=Solution()
print(s.isIsomorphic("aba","baa"))