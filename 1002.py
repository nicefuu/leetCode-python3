"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
e.g.
输入：["bella","label","roller"]
输出：["e","l","l"]
"""
class Solution:
    def commonChars(self, A):
        """
        :param A: list[str]
        :return: list[str]
        """
        flag =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        na=[]
        for i in range(len(A)):
            nflag = []
            for j in range(len(flag)):
                nflag.append(A[i].count(flag[j]))
            na.append(nflag)
        ra=[]
        m=0
        for i in range(len(na[0])):
            for j in range(len(na)):
                if j==0:
                    m=na[0][i]
                else:
                    m=min(m,na[j][i])
            ra.append(m)
        nr=[]
        for i in range(len(ra)):
            if ra[i]!=0:
                for j in range(ra[i]):
                    nr.append(chr(i+97))
        return nr

class Solution2:
    def commonChars(self, A):
        """
        :param A: list[str]
        :return: list[str]
        """
        if not A:
            return []
        res = []
        for c in set(A[0]):
            count = [w.count(c) for w in A]
            s = c * min(count)  # 如果不是每个单词都有的字母，min(count)=0
            for a in s:
                res.append(a)
        return res
s =Solution2()
a = ["bella","label","roller"]
b = ["cool","lock","cook"]
print(s.commonChars(a))
print(s.commonChars(b))




