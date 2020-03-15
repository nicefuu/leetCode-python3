"""「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；
类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        :param n: int
        :return: str
        """
        narr = ['1', '11', '21', '1211', '111221']
        if n>5:
            for _ in range(n-4):
                s = narr[-1]
                sub = []
                index = 0
                charlen = 1
                while index < len(s):
                    tempchar = s[index]
                    if index + 1 < len(s):
                        if s[index + 1] == tempchar:
                            charlen += 1
                            index += 1
                        else:
                            sub.append(s[index + 1 - charlen:index + 1])
                            charlen = 1
                            index += 1
                    else:
                        sub.append(s[index + 1 - charlen:])
                        charlen = 1
                        index += 1
                t = ''
                for i in range(len(sub)):
                    t += str(len(sub[i]))+sub[i][0]
                narr.append(t)
        return narr[n-1]
s=Solution()
for i in range(1,31):
    print(s.countAndSay(i))
