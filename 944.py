class Solution:
    def minDeletionSize(self, A) :
        """
        :param A: list[str]
        :return: int
        """
        d = 0
        for j in range(len(A[0])):
            for i in range(len(A)-1):
                if ord(A[i][j])>ord(A[i+1][j]):
                    d += 1
                    break
        return d
s = Solution()
a = ["cba", "daf", "ghi"]
b = ["a","b"]
c = ["zyx", "wvu", "tsr"]
print(s.minDeletionSize(a))
print(s.minDeletionSize(b))
print(s.minDeletionSize(c))