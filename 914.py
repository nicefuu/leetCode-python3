"""给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

 

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
示例 3：

输入：[1]
输出：false
解释：没有满足要求的分组。
示例 4：

输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
示例 5：

输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]
"""


class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        """
        :param deck:list[int]
        :return: bool
        """
        if len(deck)<=1:
            return False
        card_num = len(deck)
        min_group = len(set(deck))
        if int(card_num/min_group) <= 1:
            return False
        deck.sort()
        for group in range(min_group, int(card_num / 2) + 1):
            if card_num % group == 0:
                group_cards_num = int(card_num / group)
                k = 0
                while k < group:
                    if len(set(deck[k * group_cards_num:(k + 1) * group_cards_num])) != 1:
                        break
                    k += 1
                if k == group:
                    return True
        return False


s = Solution()
print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
print(s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
print(s.hasGroupsSizeX([1, 1, 1, 1, 2, 2]))
print(s.hasGroupsSizeX([1]))
print(s.hasGroupsSizeX([1,1]))
