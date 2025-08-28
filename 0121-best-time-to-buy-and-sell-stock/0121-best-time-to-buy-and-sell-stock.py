class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float("inf")
        maxp = 0
        for price in prices:
            if price < min:
                min = price

            profit = price - min

            if profit > maxp:
                maxp = profit
        
        return maxp

        