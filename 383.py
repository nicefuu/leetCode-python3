"""给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :param ransomNote: str
        :param magazine: str
        :return: bool
        """
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
            else:
                return False
        return True

class Solution2:
    def canConstruct(self, ransomNote, magazine):
        """
        :param ransomNote: str
        :param magazine: str
        :return: bool
        """
        flag =True
        for i in range(len(ransomNote)):
            if ransomNote.count(ransomNote[i])<=magazine.count(ransomNote[i]):
                continue
            else:
                flag=False
                break
        return flag
s=Solution2()
print(s.canConstruct("aggf","gabcfg"))