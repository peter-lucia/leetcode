class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            exists_idx = lookup.get(target-num)
            if exists_idx is not None:
                return [exists_idx, i]
            lookup[num] = i
        return [-1, -1]
        