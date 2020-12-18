class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for idx, num in enumerate(nums):
            if target-num in lookup:
                return idx, lookup[target-num]
            
            lookup[num] = idx


        