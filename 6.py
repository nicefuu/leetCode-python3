"""将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        :param s: str
        :param numRows:int
        :return: str
        """
        if len(s) <= numRows or numRows<=1:
            return s
        columns=int(len(s)/(2*numRows-2)+1)*(numRows-1)
        print(columns)
        temp = [['' for _ in range(columns)] for _ in range(numRows)]
        print(temp)
        s_index = 1
        i = 0
        j = 0
        temp[0][0]=s[0]
        while s_index < len(s):
            if j % (numRows - 1) == 0 and i != numRows - 1:
                i += 1
            else:
                i -= 1
                j += 1
            temp[i][j]=s[s_index]
            s_index += 1
        ret=''
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                ret+=temp[i][j]
        return ret



s = Solution()
# print(s.convert("LEETCODEISHIRING", 4))
# print(s.convert("AB", 1))
print(s.convert("ABCDE", 4))
