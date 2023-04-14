class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return nums[::-1]
        n = len(nums)

        left_to_right = [None for _ in range(n)]
        left_to_right[0] = nums[0]
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            left_to_right[idx] = left_to_right[idx-1]*num

        right_to_left = [None for _ in range(n)]
        right_to_left[0] = nums[-1]
        for idx, num in enumerate(nums[::-1]):
            if idx == 0:
                continue
            right_to_left[idx] = right_to_left[idx-1]*num
        right_to_left.reverse()

        result = [None for i in range(len(nums))]
        result[0] = right_to_left[1]
        result[-1] = left_to_right[-2]
        for i in range(len(nums)):
            if i == 0 or i == (len(nums) - 1):
                continue
            result[i] = left_to_right[i-1]*right_to_left[i+1]
        return result

