class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # This is a variation of the subset sum problem
        # dp[i][j] stores the number of subsets of the sub-array such that their sum is equal to j.
        # Credit: https://leetcode.com/problems/target-sum/discuss/97340/C%2B%2BPython-short-dp-solution
        
        total = sum(nums)
        n = len(nums)
        
        # impossible to acheive target by negating a subset of the numbers
        if (total + target) % 2 == 1 or abs(target) > total:
            return 0
        
        # we know now that target is even so it's divisible by 2
        # s1 contains numbers with positive signs, s2 is negative since it contains the numbers that have negative signs
        # s1 - s2 = target, 
        # s1 + s2 = total
        # s1 = (target + total) // 2
        target_sum = (total + target) // 2
        
        # consider this a black box. it's just running subset sum
        dp = [1] + [0 for _ in range(target_sum)]
        
        for num in nums:
            for s in range(target_sum, num-1, -1):
                dp[s] += dp[s - num]
        return dp[target_sum]
        
