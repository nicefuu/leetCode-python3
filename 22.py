"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]"""


class Solution:
    def __init__(self):
        self.ret = []

    def generateParenthesis(self, n):
        """
        :param n: int
        :return: list[str]
        """
        self.dfs(n, 0, 0, '')
        return self.ret

    def dfs(self, n, left, right, s):
        """
        :param left: int
        :param right: int
        :param s: str
        :return:
        """
        if left == n:
            # if s + (left - right) * ')' not in self.ret:
            self.ret.append(s + (left - right) * ')')
            return
        if left < n:
            self.dfs(n, left + 1, right, s + '(')
        if right < left:
            self.dfs(n, left, right + 1, s + ')')


class Solution2:
    def generateParenthesis(self, n):
        """
        :param n: int
        :return: list[str]
        """
        ret = []

        def dfs(n, left, right, s):
            if left == n:
                ret.append(s + (left - right) * ')')
                return
            if left > right:
                dfs(n, left, right + 1, s + ')')
            if left < n:
                dfs(n, left + 1, right, s + '(')


        dfs(n, 0, 0, '')
        return ret


s = Solution2()
print(s.generateParenthesis(3))
