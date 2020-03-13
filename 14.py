"""编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :param strs: list[str]
        :return: str
        """
        if len(strs)==0:
            return ''
        elif len(strs)==1:
            return strs[0]
        else:
            lens = []
            for i in range(len(strs)):
                lens.append(len(strs[i]))
            lens.sort()
            cnt = 0
            br=False
            for i in range(lens[0]):
                if br:
                    break
                for j in range(len(strs) - 1):
                    if strs[j][i] != strs[j + 1][i]:
                        br=True
                        break
                    if j == len(strs) - 2:
                        cnt += 1
            ret = ''
            for i in range(cnt):
                ret += strs[0][i]
            return ret


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["good","goo","goop"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix("aca,dca"))

