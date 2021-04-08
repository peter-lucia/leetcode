class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # nums = 1,2,3,4
        # A = 1, 2, 6, 
        
        n = len(nums)
        # A = the array containing the cumulative product up to each i starting from the left side and moving right
        A = []
        prod = 1
        for each in nums:
            prod *= each
            A.append(prod)
        # B = array containing the product up to each j starting from the right side and moving left
        B = []
        prod = 1
        for each in reversed(nums):
            prod *= each
            B.append(prod)
        B.reverse()
        # iterate over the array and multiply i-1 * i+1
        result = []
        for i in range(n):
            if i == 0:
                result.append(B[1])
            elif i == n-1:
                result.append(A[n-2])
            else:
                result.append(A[i-1]*B[i+1])
            
        return result            