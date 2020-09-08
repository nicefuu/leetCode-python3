#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 12:39
# @Author  : Fhh
# @File    : 1079.py
# Good good study,day day up!
"""你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

注意：本题中，每个活字字模只能使用一次。

 

示例 1：

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
示例 2：

输入："AAABBC"
输出：188
 

提示：

1 <= tiles.length <= 7
tiles 由大写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-tile-possibilities
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = dict()

        def save_result(tmp, n, titles):
            if tmp:
                res[tmp] = 1
            if len(tmp) == n:
                return
            for i in range(len(titles)):
                save_result(tmp + titles[i], n, titles[:i] + titles[i + 1:])

        save_result('', len(tiles), tiles)
        return len(res)


s = Solution()
print(s.numTilePossibilities("AAABBC"))
