class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = [-1, -1]
        for idx, num in enumerate(nums):
            if num == target and result[0] == -1:
                result = [idx, idx]
            elif num == target and result[0] != -1:
                result[1] = idx

        return result
            