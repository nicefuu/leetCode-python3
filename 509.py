class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return self.fib(N-2) + self.fib(N-1)
class Solution2:
    def fib(self,N):
        f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        return f[N]
s1 = Solution()
s2 = Solution2()
cnt=0
for i in range(31):
    if s1.fib(i)==s2.fib(i):
        cnt+=1
print(cnt)