class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # we can assume n > 2
        n = len(nums)
        
        products_left = []
        running_product = 1
        for i in range(n):
            running_product *= nums[i]
            products_left.append(running_product)
        
        products_right = []
        running_product = 1
        for i in range(n-1, -1, -1):
            running_product *= nums[i]
            products_right.append(running_product)
        
        products_right.reverse()
        
        result = [0]*n
        result[0] = products_right[1]
        result[n-1] = products_left[n-2]
        for i in range(1, n-1):
            result[i] = products_right[i+1]*products_left[i-1]
        
        return result
        