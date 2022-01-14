class Solution:
    def superPow(self, x: int, b: List[int]) -> int:
        N = 1337
        y = int("".join([str(each) for each in b]))
        
        y = deque([int(digit) for digit in bin(y)[2:]])
        
        num = y.popleft()
        assert num == 1
        result = x
        
        while y:
            num = y.popleft()
            if num == 0:
                result = (result*result) % N
            else:
                result = (result*result) % N
                result = (result*x) % N
        return result
            
            
            
                
                
            
        
        
        