"""给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。

示例 1：

输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：A = "apple apple", B = "banana"
输出：["banana"]
"""
class Solution:
    def uncommonFromSentences(self, A, B) :
        """
        :param A:str
        :param B: str
        :return: list[str]
        """
        a=A.split()
        sa=(set(a))
        b=B.split()
        sb=set(b)
        rt=[]
        for i in sa:
            if (i not in sb) and a.count(i)==1:
                rt.append(i)
        for i in sb:
            if (i not in sa) and b.count(i)==1:
                rt.append(i)
        return rt
class Solution2:
    def uncommonFromSentences(self, A, B) :
        """
        :param A:str
        :param B: str
        :return: list[str]
        """
        a=(A+' '+ B).split()
        rt=[]
        for i in set(a):
            if a.count(i)==1:
                rt.append(i)
        return rt
s=Solution2()
print(s.uncommonFromSentences("this apple is sweet","this apple is sour"))
print(s.uncommonFromSentences("apple apple","banana"))