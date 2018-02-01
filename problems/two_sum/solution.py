class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tried = {}
        for i in range(0, len(nums)):
            a = nums[i]
            neededNum = target - a
            if neededNum in tried:
                return [tried[neededNum], i]
            #if neededNum in nums:
            #    j = nums.index(neededNum)
            #    if i != j:
            #        return [i, j]
            tried[a] = i
        return []
        