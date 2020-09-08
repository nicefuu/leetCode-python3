#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 23:28
# @Author  : Fhh
# @File    : 139.py
# @Software: PyCharm
# good good study,day day up!
"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
    注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import time

class Solution:
    def wordBreak(self, s, wordDict: List[str]):
        d = dict()
        for word in wordDict:
            d[word] = True
        dp = [False for _ in range(len(s) + 1)]
        for i in range(1, len(dp) + 1):
            for j in range(i):
                if dp[j] and d[s[j:i]]:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == '__main__':
    start=time.time()
    s = Solution()
    s1 = "aaaaaaaa"
    wordDict = ["aaa", "aaaa"]

    print(s.wordBreak(s1, wordDict))