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

    def generateParenthesis(self, n):
        """
        :param n: int
        :return: list[str]
        """
        res = []

        def back(tmp, left, right, n):
            if left == n:
                tmp += ')' * (left - right)
                res.append(tmp)
                return
            if left < n:
                back(tmp + '(', left + 1, right, n)
            if right < left:
                back(tmp + ')', left, right + 1, n)

        back('', 0, 0, n)
        return res


s = Solution()
print(s.generateParenthesis(2))
