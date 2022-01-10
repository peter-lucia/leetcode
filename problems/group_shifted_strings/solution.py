class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Approach
        # Shift each string until the starting character is a
        # If the shifted string is in the lookup of previously shifted strings
        # then append it to the list of strings for that key
        # Repeat for all strings
        
        
        lookup = defaultdict(list)
        
        def shift(key: str) -> str:
            # shifts a string until starting character is 'a'
            
            if key[0] != 'a':
                diff = ord(key[0]) - ord('a')
                result = []
                for c in key:
                    c_shifted = ord(c) - diff
                    if c_shifted < ord('a'):
                        c_shifted = ord('z') - (ord('a') - c_shifted) + 1
                    result.append(chr(c_shifted))
                result = "".join(result)
            else:
                result = key
            return result
        
        for s in strings:
            s_shifted = shift(s)
            lookup[s_shifted].append(s)
            
        return lookup.values()
                
            