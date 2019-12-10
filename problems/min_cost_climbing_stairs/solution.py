class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dynamic programming approach
        
        previous_sum = next_sum = 0
        for each in reversed(cost):
            temp_sum = next_sum
            next_sum = each + min(previous_sum, next_sum)
            previous_sum = temp_sum
            
        return min(previous_sum, next_sum)