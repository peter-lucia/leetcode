class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Brute force solution O(n^2)
        # Need to consider all possible contiguous subsequences
        # i: 0 -> n-1
        # j: 0 -> i-1
        # max_sum = max(max_sum, nums[j:i])
        
        # Greedy approach O(n)
        # base case: 
        # empty array dp[0] = max(nums[0], 0)
        
        # for i = 1 -> n-1:
        #    max_sum = max(dp[i-1] + nums[i], nums[i]) 
        
        # nums = [-2, 1, 7, 2, 9]
        # dp   = [0,  0, 0, 0, 0] 
        #        [0,  1, 8, 10, 19]
        
        # nums = [-2, 1, 7, -3, 1, 1]
        # dp   = [ 0, 0, 0,  0, 0, 0]
        #      = [ 0, 0, 0,  0, 0, 0] max(-2, 0) = 0
        #      = [ 0, 1, 0,  0, 0, 0] max(0, 1) = 1
        #      = [ 0, 1, 8,  0, 0, 0] max(1+7, 7) = 8
        #      = [ 0, 1, 8,  5, 0, 0] max(5, -3) = 5
        #      = [ 0, 1, 8,  5, 6, 0] max(6, 1) = 6
        #      = [ 0, 1, 8,  5, 6, 7]  max(7, 1) = 7
        
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        # Base case
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            
        return max(dp)
            
            
        
        