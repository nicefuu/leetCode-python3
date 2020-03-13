"""
给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

示例 1:

输入: S = "loveleetcode", C = 'e'
输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :param S: str
        :param C: str
        :return: list[int]
        """
        cindex = []#记录C在S中的索引
        rarr=[]
        for i in range(len(S)):
            if S[i] == C:
                cindex.append(i)
        m=len(S)
        for i in range(len(S)):
            for j in cindex:
                m=min(m,abs(i-j))
            rarr.append(m)
            m=len(S)
        return rarr
s=Solution()
str =  "loveleetcode"
c= "e"
print(s.shortestToChar(str,c))
