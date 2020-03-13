"""给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。"""
class Solution:
    def addBinary(self, a, b):
        """
        :param a: str
        :param b: str
        :return: str
        """
        if len(a)>len(b):
            x=a
            y=b
        else:
            x=b
            y=a
        #x为长串 y为短串
        while len(x)>len(y):
            y = '0' + y
        x="0"+x
        y="0"+y
        n = len(x)-1
        z=''
        p=0
        while n>=0:
            if int(x[n])+int(y[n]) + p ==0:
                z = '0' + z
                p = 0
            elif int(x[n])+int(y[n]) + p ==1:
                z = '1' + z
                p = 0
            elif int(x[n])+int(y[n]) + p==2:
                z = '0' + z
                p = 1
            elif int(x[n])+int(y[n]) + p ==3:
                z = '1' + z
                p = 1
            n -= 1
        if z[0]=='0':
            z = z[1:]
        return z



a="0"
b="0"
s=Solution()
print(s.addBinary(a,b))
