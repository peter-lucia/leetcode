class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)

        results = set()
        for left in range(n):
            # Since all numbers after left are larger, if it's > 0, we have to stop
            if nums[left] > 0:
                break

            middle = left + 1
            right = n - 1
            while middle < right and right < n:
                if nums[left] + nums[middle] + nums[right] < 0: # sum is too small
                    middle += 1
                elif nums[left] + nums[middle] + nums[right] > 0: # sum is too large
                    right -= 1
                else:
                    results.add((nums[left], nums[middle], nums[right]))
                    # only shot we have is by both increasing and decreasing total potential sum
                    middle += 1 
                    right -= 1

        return list(results)

