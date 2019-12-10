class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_gain = 0
        if len(prices) <= 1:
            return max_gain
        min_price = prices[0]
        for i in range(1, len(prices)):
            gain = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            elif gain > max_gain:
                max_gain = gain
        return max_gain
        
            
            
            
                
            