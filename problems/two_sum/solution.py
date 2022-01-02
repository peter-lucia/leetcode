class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in lookup:
                return i, lookup[target - num]
            lookup[num] = i
        return [-1, -1]
            
        