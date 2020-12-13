class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        nums = [int(num) for num in s]
        
        n = len(s)
        if n == 0:
            return 0
        if nums[0] == 0:
            return 0
        
        T = [0 for _ in range(n+1)]
        
        T[0] = 1
        
        if n == 1:
            return 1
        
        T[1] = 0 if nums[1] == 0 else 1
        
        for i in range(2, len(T)):
            if nums[i-1] != 0:
                T[i] += T[i-1]
                           
            if (10 <= nums[i-2]*10 + nums[i-1] <= 26):
                T[i] += T[i-2]

            
        return T[n]
        
        