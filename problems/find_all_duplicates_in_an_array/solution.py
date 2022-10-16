class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        nums.sort()

        if len(nums) < 2:
            return []
        elif len(nums) == 2 and nums[0] == nums[1]:
            return [nums[0]]

        result = []

        for i in range(2, len(nums)):
            curr = nums[i]
            prev_prev = nums[i-2]
            prev = nums[i-1]
            if curr != prev and (prev == prev_prev):
                result.append(prev)
            elif curr == prev and (prev != prev_prev) and i == len(nums) - 1:
                result.append(curr)
            elif curr == prev and (prev == prev_prev):
                pass
            elif curr != prev and (prev != prev_prev):
                pass
        return result
               




