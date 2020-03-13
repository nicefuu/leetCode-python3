class Solution:
    def calPoints(self, ops):
        score = []
        cnt = 0
        for i in ops:
            if i == '+':
                score.append(int(score[-1]) + int(score[-2]))
            elif i == 'D':
                score.append(int(score[-1]) * 2)
            elif i == 'C':
                del score[-1]
            else:
                score.append(i)
        for i in score:
            cnt += int(i)
        return cnt
s= Solution()

a = ["5","2","C","D","+"]
b = ["5","-2","4","C","D","9","+","+"]
c = ["36","28","70","65","C","+","33","-46","84","C"]
print(s.calPoints(a))
print(s.calPoints(b))
print(s.calPoints(c))