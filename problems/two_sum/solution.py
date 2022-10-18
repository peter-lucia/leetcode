class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}

        for idx, val in enumerate(nums):
            num = target - val
            i = lookup.get(num, None)
            if i is not None:
                return [i, idx]
            lookup[val] = idx
        
        return [-1, -1]
            
