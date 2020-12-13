class Solution:    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        if n == 0:
            return 0
        
        characters = set()
        mx = i = j = 0
    
        while i < n and j < n:
            if s[j] not in characters:
                characters.add(s[j])
                j += 1
                mx = max(mx, j-i)
            else:
                characters.remove(s[i])
                i += 1
         
        return mx
                
        
        
        
        
        