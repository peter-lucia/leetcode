class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        
        nums.sort()
        # replace the first three
        max_diff_1 = nums[-1] - nums[3]
        
        # replace the last three
        max_diff_2 = nums[-4] - nums[0]
    
        # replace the first 2, then the last number
        max_diff_3 = nums[-2] - nums[2]
        
        # replace the first num, then the last 2
        max_diff_4 = nums[-3] - nums[1]
        
        return min(max_diff_1, max_diff_2, max_diff_3, max_diff_4)
