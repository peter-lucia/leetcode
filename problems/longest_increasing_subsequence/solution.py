class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # array containing the length of the LIS up to each element
        arr = [0 for _ in nums]
        
        for i, x in enumerate(nums):
            # holds the maximum LIS up to and including x
            m = 0 
            for j in range(0, i):
                # check if current x is greater than each previous element, 
                # starting at the first element in the array.
                # also check if the max length of the LIS up to each
                # preceding element is at least m
                # if x > nums[j] and arr[j] >= m:
                if x > nums[j] and arr[j] >= m:
                    m = arr[j]

            arr[i] = m + 1
        return max(arr)
