class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        a_letters = deque([each for each in A])
        a_length = len(a_letters)
        b_letters = deque([each for each in B])
        for i in range(a_length+1):
            if a_letters == b_letters:
                return True
            a_letters.rotate(-1)
            
        return False
        
              
            
            
            
        
            
        