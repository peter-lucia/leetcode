class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        
        
        last_num = nums[0]
        for i in range(1, n):
            if nums[i] == last_num:
                return True
            last_num = nums[i]
        return False