class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        
        # Approach / Observations
        
        # Use a lookup to put all valid replacements in
        # Iterate through the characters in the string, if the index is in the lookup
        # add the replaced target to the result instead of the original source
        # increment idx by the length of the source text that was replaced
        # if the index is not in the lookup, add the character to the result and increment
        # the idx by one
        
        # Example:
        # abcd
        # indices = [0,2]
        # sources = ["a", "cd"]
        # targets = ["eee", "ffff"]
        
        lookup = {}
        
        for i in range(len(indices)):
            start_idx = indices[i]
            source_word = sources[i]
            if s[start_idx:start_idx + len(source_word)] == source_word:
                lookup[start_idx] = (sources[i], targets[i])
                
        result = ""
        i = 0
        while i < len(s):
            if i in lookup:
                result += lookup[i][1]
                i += len(lookup[i][0])  # 
            else:
                result += s[i]
                i += 1
        return result
                
                
        
        
        
        