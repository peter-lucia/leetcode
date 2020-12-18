class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        if n == 0:
            return []
        # O(nlogn)
        nums = sorted(nums)
        
        result = []

        for i in range(n):
            if nums[i] > 0:
                break
                
            if i == 0 or nums[i-1] != nums[i]:
                
                j, k = i+1, n-1
                

                while j < k:
                    _sum = nums[i] + nums[j] + nums[k]
                    if _sum < 0:
                        j += 1
                    elif _sum > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j-1] == nums[j]:
                            j += 1

        return result