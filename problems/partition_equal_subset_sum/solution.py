class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # Observations / Notes / Ideas
        
        # Brute force: find all subsets of the array, return true if there is at least one duplicate
        # Can add all subsets to a set. If the length of the set is less than the length of nums,
        # then there is a duplicate
        
        # how many possible permutations of the array are there into size k?
        # n! / (n - k)!
        # there are also n-1 possible places to split for each permutation of the array
        # so (n-1) * (n!/(n-k)!) where k = n-1 for two split positions since we 
        # (n-1)*(n!/1!) = n^2*(n-1)! which is pretty horrible.
        # maybe memoization could help?
        
        # Approach #1 (Dynamic Programming)
        
        # dp[i][j] = True if the sum j can be formed by array elements in subsets nums[0]...nums[i]
        # otherwise, dp[i][j] = False
        #    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22
        # '' 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        # 1  1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        # 5  1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        # 11 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0
        # 5  1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1
        
        n = len(nums)
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        dp = [[False for _ in range(total+1)] for _ in range(n+1)]
        
        # if no elements and no total, we can always get desired sum of 0
        dp[0][0] = True
        
        for ii in range(1, n+1):
            for jj in range(total+1):
                i = ii - 1
                # if current total is less than current number in nums
                # then we could only make jj if that was possible without using nums[i]
                if jj < nums[i]:
                    dp[ii][jj] = dp[ii-1][jj]
                # current total is >= nums[i], so mark True if it was already possible without nums[i]
                # or make true if jj - nums[i] was possible without using nums[i]
                else:
                    dp[ii][jj] = dp[ii-1][jj] or dp[ii-1][jj- nums[i]]
        #for row in dp:
        #    print(([int(each) for each in row]))
        return dp[n][total // 2]
                    
                
                
        
        