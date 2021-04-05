class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = set([each for each in range(1, n+1)])
        
        for each in nums:
            if each in result:
                result.remove(each)
            
        return result