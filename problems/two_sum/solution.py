#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use hash table (dictionary) to get linear time complexity
        tried = {}
        for idx, num in enumerate(nums):
            neededNum = target - num
            if neededNum in tried:
                return [tried[neededNum], idx]
            tried[num] = idx
        return []

s = Solution()
