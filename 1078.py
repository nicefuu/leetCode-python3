"""给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

示例 1：

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]
示例 2：

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        """
        :param text: str
        :param first: str
        :param second: str
        :return: list[str]
        """
        rt = []
        s = text.split()
        if len(s)>=3:
            for i in range(len(s) - 2):
                if s[i] == first and s[i + 1] == second:
                        rt.append(s[i + 2])
        return rt


ss = Solution()
print(ss.findOcurrences(text="alice is a good girl she is a good student", first="a", second="good"
                        ))
print(ss.findOcurrences(text = "we will we will rock you", first = "we", second = "will"
                        ))
