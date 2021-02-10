class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        max_profit = 0
        bought_stock = -prices[0]
        for i in range(n):
            if bought_stock + prices[i] - fee > max_profit:
                max_profit = bought_stock + prices[i] - fee
            if max_profit - prices[i] > bought_stock:
                bought_stock = max_profit - prices[i]
            
        return max_profit