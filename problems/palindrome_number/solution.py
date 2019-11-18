class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = str(x)
        val = [each for each in val]
        temp = val.copy()
        val.reverse()
        if temp == val:
            return True
        return False
        