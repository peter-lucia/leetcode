class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        """
        Let L = the length of the longest increasing subsequence 
        from a_1 to a_i.
        
        if nums[i]
        """
        T = [1 for _ in range(n)]
        
        for i in range(n):
            xi = nums[i]
            for j in range(i):
                xj = nums[j]
                if xi > xj and T[i] < T[j] + 1:
                    T[i] = 1 + T[j]


                    
        return max(T)