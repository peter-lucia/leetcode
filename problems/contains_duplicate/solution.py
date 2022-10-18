class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()
        
        last_val = None

        for num in nums:
            if last_val == num:
                return True
            last_val = num
        return False