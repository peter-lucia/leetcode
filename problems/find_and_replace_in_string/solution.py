class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Time complexity: O(nk) where n is the number of sources and k is the max size of a string
        # Space complexity: O(nk) to house potentially all source and replacement texts
        
        # Key ideas
        
        # 1. Create a lookup of mapping an index to a source that was found in s with its replacement text
        # e.g. for s = "abcd", indices = [0,2], sources = ["ab", "cd"], targets = ["eeee", "bbbb"]
        # lookup = {
        #   starting_idx: [source text, replacement text]
        #     0: ["ab", "eeee"] 
        #     2: ["cd", "bbbb"] 
        # }
        
        # 2. Replace the found sources with their targets
        #    If the current index is not in the lookup, just add the character in s at index to the result
        #    If the current index is in the lookup, replace its source and increment index by len(source)
        
        letters = defaultdict(str)
        for idx, each in enumerate(s):
            letters[idx] = each
        
        lookup = {}
        for i, source in enumerate(sources):
            if source == s[indices[i]:indices[i] + len(source)]:
                lookup[indices[i]] = [source, targets[i]]
        
        result = ""
        idx = 0
        while idx < len(s) or idx in lookup:
            if idx in lookup:
                result += lookup[idx][1]
                idx += len(lookup[idx][0])
            else:
                result += s[idx]
                idx += 1
        return result
            
            
        