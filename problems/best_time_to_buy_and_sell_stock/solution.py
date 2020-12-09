class Solution:
    
    def getMaxProfit(self, prices: List[int]) -> (int, int, int):
        if len(prices) == 1:
            return 0, prices[0], prices[0]
        n = len(prices)
        
        pA, minA, maxA = self.getMaxProfit(prices[:n//2])
        pB, minB, maxB = self.getMaxProfit(prices[(n//2):])
        
        return max(pA, pB, maxB - minA), min(minA, minB), max(maxA, maxB)
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        return self.getMaxProfit(prices)[0]

        
        