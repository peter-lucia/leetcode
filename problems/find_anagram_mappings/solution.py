class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        lookup = {}
        for idx, each in enumerate(B):
            lookup[each] = idx
        result = [0] * len(A)
        for idx, each in enumerate(A):
            result[idx] = lookup.get(each, -1)
        return result
        
            