class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        i = 0
        j = 1
        vals = set([s[i]]) 
        max_size = 1

        while j < len(s):
            if s[j] not in vals:
                vals.add(s[j])
                j += 1
            else:
                vals.discard(s[i])
                i += 1
            max_size = max(max_size, len(vals))
        return max_size
        
