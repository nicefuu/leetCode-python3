"""
给你一个仅由数字 6 和 9 组成的正整数 num。
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
请返回你可以得到的最大数字。
示例 1：
输入：num = 9669
输出：9969
解释：
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        :param num: int
        :return: int
        """
        num_list = list(str(num))
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break
        return int(''.join(num_list))


class Solution2:
    def maximum69Number(self, num: int) -> int:
        """
        :param num: int
        :return: int
        """
        return int(str(num).replace('6','9',1))

s = Solution2()
a = 9699
print(s.maximum69Number(a))
