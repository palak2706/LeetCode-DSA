# LeetCode 121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array, Greedy

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                profit = max(profit, price - buy)

        return profit


# Time Complexity: O(n)
# Space Complexity: O(1)