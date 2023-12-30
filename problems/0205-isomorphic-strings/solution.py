class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if each character c in s is not in the lookup
        # map it to the character in t at the same index as c
        # if it is in the lookup, check that the element at that index in t
        # is the same element that is already mapped to in the lookup
        # if it is not, return False,
        # if it is continue
        # at the end, return True

        if len(s) != len(t):
            return False
        
        if len(set(s)) != len(set(t)):
            return False

        lookup = {}
        for i, c in enumerate(s):
            if lookup.get(c) is None:
                lookup[c] = t[i]
            elif lookup.get(c) != t[i]:
                return False
        return True
                




        
