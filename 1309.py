"""给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
字符（'a' - 'i'）分别用（'1' - '9'）表示。
字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
返回映射之后形成的新字符串。
题目数据保证映射始终唯一。
示例 1：
输入：s = "10#11#12"
输出："jkab"
解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
示例 2：
输入：s = "1326#"
输出："acz"
#a-z 97-122
#0-9 48-57
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        :param s: str
        :return: str
        """
        t = []
        for i in range(len(s)):
            if s[i] != '#':
                t.append(chr(ord(s[i]) + 48))  # 1=a 2=b
            else:
                temp = (ord(t[-2]) - 96) * 10 + ord(t[-1]) - 96
                del t[-1]
                t[-1] = chr(temp + 96)
        return (''.join(t))


class Solution2:
    def freqAlphabets(self, s: str) -> str:
        """
        :param s: str
        :return: str
        """
        rs = s[::-1]
        t = []
        i = 0
        while i < len(s):
            if rs[i] == '#':
                t.append(chr(int(rs[i + 1]) + int(rs[i + 2]) * 10 + 96))
                i += 3
            else:
                t.append(chr(int(rs[i]) + 96))
                i += 1
        return ''.join(t[::-1])


s = Solution2()
print(s.freqAlphabets("121212"))
