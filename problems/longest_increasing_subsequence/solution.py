class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        n = len(nums)
        
        L = [0 for _ in range(n)]
        for i in range(0, n):
            m = 0
            for j in range(0, i):
                if nums[i] > nums[j] and L[j] >= m:
                    m = L[j]
            L[i] = m + 1
            
        return max(L)
            
            
