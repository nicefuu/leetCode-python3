"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""


class Solution:
    def letterCombinations(self, digits: str):
        """
        :param digits:str
        :return: list[str]
        """
        if len(digits)==0:
            return []
        keymap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []

        def dfs(tmp, digits, index):
            """
            :param tmp:str
            :param digits:str
            :param index:int
            :return: None
            """
            if index == len(digits):
                res.append(tmp)
                return
            for i in range(len(keymap[int(digits[index])])):
                # len(keymap[int(digits[index])])为按键digit[index]上的字符数(字符串长度)
                dfs(tmp + keymap[int(digits[index])][i], digits, index + 1)

        dfs("", digits, 0)
        return res


s = Solution()
print(s.letterCombinations('234'))
