class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        i = 0
        j = 1
        profit = 0
        while j < n:
            if prices[j] > prices[i]:
                profit += prices[j] - prices[i]
                i = j
                j += 1
            else:
                i = j
                j = j+1
            
                
        return profit
        
        