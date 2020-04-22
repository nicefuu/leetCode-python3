#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 9:30
# @Author  : Fhh
# @File    : 459.py
# Good good study,day day up!
"""给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
示例 2:
输入: "aba"
输出: False
示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        :param s:str
        :return: bool
        """
        if not s:
            return False
        if len(s) == 1:
            return True
        for i in range(len(s) - 1, 0, -1):
            if len(s) % i == 0:
                sublen = len(s) // i
                tmp = []
                for k in range(sublen):
                    tmp.append(s[k * i:(k + 1) * i])
                if len(set(tmp)) == 1:
                    return True
        return False


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        :param s:str
        :return: bool
        """
        """假设母串S是由子串s重复N次而成，
         则S+S则有子串s重复2N次,现在S=Ns，
          S+S=2Ns 因此S在(S+S)[1:-1]中必出现一次以上"""
        return s in (s + s)[1:-1]


s = Solution()
print(s.repeatedSubstringPattern("abcabcabc"))
