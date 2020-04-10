#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 19:57
# @Author  : Fhh
# @File    : 345.py
# Good good study,day day up!
"""编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
示例 1:
输入: "hello"
输出: "holle"
示例 2:
输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        :param s:str
        :return: str
        """
        arrs=list(s)
        indices=[]
        words=[]
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                indices.append(i)
                words.append(s[i])
        indices=indices[::-1]
        for i in range(len(indices)):
            arrs[indices[i]]=words[i]
        return ''.join(arrs)
s=Solution()
a='aA'
print(s.reverseVowels(a))

