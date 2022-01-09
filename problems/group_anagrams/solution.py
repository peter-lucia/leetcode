class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Approach #1: create lookup for each word
        # Map sorted version of the string to list of matching strings 
        # Return a list of list of values at the end grouped by key
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        result = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            result[key].append(s)
            
        return result.values()
            
            
                
            
            
            
        
        