#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:36
# @Author  : Fhh
# @File    : 122.py
# Good good study,day day up!
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
提示：
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4"""


class Solution:
    def maxProfit(self, prices) -> int:
        """
        :param prices:list[int]
        :return: int
        """
        if not prices or len(prices) < 2:
            return 0
        profit = 0
        day_in, day_out = 0, 0
        while day_in < len(prices) - 1:
            if prices[day_in + 1] <= prices[day_in]:
                day_in += 1
                continue
            else:
                day_out = day_in + 1
                while day_out < len(prices) - 1:
                    if prices[day_out + 1] >= prices[day_out]:
                        day_out += 1
                    else:
                        break
                profit+=prices[day_out]-prices[day_in]
                day_in=day_out+1
        return profit

s=Solution()
a=[7,1,5,3,6,4]
b=[1,2,3,4,5]
c=[7,6,4,3,1]
print(s.maxProfit(a))
print(s.maxProfit(b))
print(s.maxProfit(c))
