class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        j = 1
        i = 0
        
        while k < len(nums):
            if nums[i] == nums[j] \
              == nums[k]:
                nums.pop(k)
                k -= 1
                j -= 1
                i -= 1
            i += 1
            j += 1
            k += 1
        
        


        
