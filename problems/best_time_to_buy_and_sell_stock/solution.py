class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # keep track of min price
      # calc gain at each i
      # compare to max gain
      p = prices
      if not p:
        return 0
      mgain = 0
      mprice = p[0]
      for i in range(1,len(p)):
        gain = p[i] - mprice
        mprice = min(
          mprice, p[i]
        )
        mgain = max(
          mgain,
          gain
        )
      return mgain

        