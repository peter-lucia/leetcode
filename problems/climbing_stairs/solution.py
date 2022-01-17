class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0 for _ in range(n+1)]
        
        dp[0] = 1  # one way to cover dist of 0 via 0 steps
        if n >= 1:
            dp[1] = 1  # one way to cover dist of 1 via 1 step
        if n >= 2:
            dp[2] = 2  # two ways to climb 2 steps via a 2 step or two single steps
        
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
        