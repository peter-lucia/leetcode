class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = index of last unique num
        # j = index of current num

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1


        
