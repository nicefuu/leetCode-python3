"""给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""
"""
d[i][j]表示第一个单词的前i位变成第二个单词的前j位所需要的编辑距离（即最小操作次数）
第一个单词的前i位变成第二个单词的前j-1位，然后再插入一个字符（d[i][j-1]+1）
第一个单词的前i-1位变成第二个单词的前j位，然后再删去一个字符（d[i-1][j]+1）
第一个单词的前i-1位变成第二个单词的前j-1位，然后替换最后一个字符，如果最后一
个字符相同，即第一个单词的第i位和第二个单词的第j位相同的话，就不用替换了（d[i-1][j-1]）
，反之，如果不同就替换最后一位（d[i-1][j-1]+1）
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        :param word1:str
        :param word2:str
        :return:int
        """
        if len(word1) * len(word2) == 0:
            return len(word1) + len(word2)
        d = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            d[i][0] = d[i - 1][0] + 1
        for j in range(1, len(word2) + 1):
            d[0][j] = d[0][j - 1] + 1
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:#第i个字符下标位i-1
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1
        return d[len(word1)][len(word2)]


s = Solution()
print(s.minDistance(word1="intention", word2="execution"))
print(s.minDistance(word1="horse", word2="ros"))
