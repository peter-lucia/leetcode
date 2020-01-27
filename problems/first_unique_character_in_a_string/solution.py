class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}
        for c in s:
            lookup[c] = lookup.get(c, 0) + 1
            
        for idx, c in enumerate(s):
            if lookup[c] == 1:
                return idx
            
        return -1
        