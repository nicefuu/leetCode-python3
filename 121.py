"""给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润
注意：你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


class Solution:
    def maxProfit(self, prices) -> int:
        """
        :param prices:list[int]
        :return: int
        """
        if not prices or len(prices) < 2:
            return 0
        day_in = 0
        day_out = len(prices) - 1
        profit = 0
        while day_in < day_out:
            profit = max(prices[day_out] - prices[day_in], profit)
            while prices[day_in + 1] < prices[day_in]:
                day_in += 1
            while prices[day_out - 1] > prices[day_out]:
                day_out -= 1


        return profit


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 4, 2]))
