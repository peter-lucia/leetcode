class Solution:
    def isEven(self, num:str):
        if len(num) % 2 == 0:
            return True
        return False
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if self.isEven(str(num)):
                result += 1
            
        return result