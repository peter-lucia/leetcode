class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,3,4,0]
        prefix array: product of nums from left to right
        [1,2,6,24,0]

        postfix array: product of nums from right to left
        [0,0,0,0,0]

        result[i] = prefix[i-1] * postfix[i+1]
        """
        n = len(nums)
        prefix = 1
        prefix_arr = [None for _ in range(n)]
        for i, each in enumerate(nums):
            prefix_arr[i] = prefix * each
            prefix = prefix_arr[i]

        postfix = 1
        postfix_arr = [None for _ in range(n)]
        for i in range(n-1, -1, -1):
            postfix_arr[i] = postfix * nums[i]
            postfix = postfix_arr[i]

        result = [None for _ in range(n)]
        for i in range(n): 
            if i == 0:
                result[i] = postfix_arr[i+1]
            elif i == n - 1:
                result[i] = prefix_arr[i-1]
            else:
                result[i] = prefix_arr[i-1] * postfix_arr[i+1]
        return result


