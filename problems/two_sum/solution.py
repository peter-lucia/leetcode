class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = {}
        for idx, num in enumerate(nums):
            other_idx = lookup.get(target-num)
            if other_idx is not None:
                return [idx, other_idx]
            lookup[num] = idx
        return [-1, -1]

