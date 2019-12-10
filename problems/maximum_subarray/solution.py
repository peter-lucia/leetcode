class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = max_sum = nums[0]
        
        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum