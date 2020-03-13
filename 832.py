class Solution:
    def flipAndInvertImage(self, A):
        for i in A:
            i.reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] += 1
                if A[i][j] == 2:
                    A[i][j] -= 2
        return A

class Solution2:
    def flipAndInvertImage(self, A):
        return [[j ^ 1 for j in i[::-1]] for i in A]
s= Solution2()
a = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(s.flipAndInvertImage(a))