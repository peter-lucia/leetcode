class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_gain = 0
        if len(prices) <= 1:
            return max_gain
        min_price = prices[0]
        for i in range(1, len(prices)):
            gain = prices[i] - min_price
            min_price = min(min_price, prices[i])
            max_gain = max(max_gain, gain)
        return max_gain