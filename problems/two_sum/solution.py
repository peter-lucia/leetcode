class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table = {}
        for idx, num in enumerate(nums):
            needed_num = target - num
            if needed_num in hash_table:
                return [idx, hash_table[needed_num]]
            else:
                hash_table[num] = idx
        return []
        