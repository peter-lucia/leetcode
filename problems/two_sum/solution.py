class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for idx, num in enumerate(nums):
            needed_num = target - num
            if needed_num in lookup:
                return [lookup[needed_num], idx]
            lookup[num] = idx
        return [-1, -1]
        