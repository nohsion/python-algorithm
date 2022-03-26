# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟갑과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(price - min_price, profit)

        return profit