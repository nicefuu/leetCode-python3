"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
"""
class Solution:
    def toLowerCase(self, str):
        """
        :param str:str
        :return:str
        """
        s = list(str)
        ns=''
        for i in range(len(s)):
            if 65<=ord(s[i])<=90:
                s[i]=chr(ord(s[i]) + 32)
            ns += s[i]
        return ns
s=Solution()
a="Hello@#$WOEDF"
#s.toLowerCase(a)
print(s.toLowerCase(a))