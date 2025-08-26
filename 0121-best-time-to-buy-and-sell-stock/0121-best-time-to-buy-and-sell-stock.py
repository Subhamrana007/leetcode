import math

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit from a single stock buy and sell.

        This function uses a single pass to find the maximum profit by keeping
        track of the lowest price encountered so far.

        Args:
            prices: A list of integers representing the stock prices on consecutive days.

        Returns:
            The maximum possible profit. Returns 0 if no profit can be made.
        """
        # Initialize the minimum price to a very large number.
        min_price = math.inf
        # Initialize the maximum profit to 0.
        max_profit = 0

        # Iterate through each price in the list.
        for price in prices:
            # Update the minimum price if the current price is lower.
            # This represents the best potential buy point so far.
            min_price = min(min_price, price)
            
            # Calculate the current potential profit if we sold at the current price.
            current_profit = price - min_price
            
            # Update the maximum profit if the current profit is higher than
            # any profit we've seen before.
            max_profit = max(max_profit, current_profit)
        
        return max_profit
