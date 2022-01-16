class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # array containing the length of the LIS up to each element
        dp = [1 for _ in nums]

        for i in range(len(nums)):
            # _max holds the maximum LIS up to and including nums[i]
            _max = 0
            for j in range(0, i):
                # check if nums[i] is greater than each previous element,
                # starting at the first element in the array.
                # keep track of length of LIS up to i with _max
                if nums[i] > nums[j]:
                    _max = max(_max, dp[j])

            # add 1 to account for nums[i]
            dp[i] = _max + 1
        return max(dp)