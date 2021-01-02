class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        
        x = str(abs(x))
        result = 0
        for i in range(len(x)):
            result += int(x[i])*10**(i)
            
        if result < -2**31 or result > 2**31 - 1:
            return 0
        if negative:
            return -result
        return result
        
        
        
            