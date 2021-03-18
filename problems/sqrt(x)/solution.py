class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        low = 2
        high = x // 2
        
        while low <= high:
            mid = (low + high) // 2
            squared = mid**2
            if squared > x:
                high = mid-1
            elif squared < x:
                low = mid+1
            else:
                return mid
            
        return high
    
        
        