#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 16:17
# @Author  : Fhh
# @File    : 49.py
# Good good study,day day up!
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""


class Solution:  # 字典表示
    def groupAnagrams(self, strs):
        """
        :param strs:list[str]
        :return:list[list[str]]
        """
        hashmap = {}
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
                'x': 23, 'y': 24, 'z': 25}
        for s in strs:
            tmp = [0 for _ in range(26)]
            for j in range(len(s)):
                tmp[dict[s[j]]] += 1
            t = tuple(tmp)
            if t in hashmap:
                hashmap[t] += [s]
            else:
                hashmap[t] = [s]
        return list(hashmap.values())


class Solution2:  # 字符串排序
    def groupAnagrams(self, strs):
        """
        :param strs:list[str]
        :return:list[list[str]]
        """
        dict_res = {}
        for s in strs:
            list_tmp = sorted(list(a))
            str_tmp = ''.join(list_tmp)
            if str_tmp in dict_res:
                dict_res[str_tmp].append(s)
            else:
                dict_res[str_tmp] = [s]
        return list(dict_res.values())


s = Solution2()
a = ["eat", "tea", "tan", "ate", "nat", "bat", "hello", "olleeh"]
print(s.groupAnagrams(a))
