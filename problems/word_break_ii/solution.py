class Solution:
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        result = []
        for word in wordDict:
            if not s.startswith(word):
                continue
                
            # s starts with current word and is the same length
            if len(word) == len(s): 
                result.append(word)
            else:
                start_idx = len(word)
                
                # recursively get result for remaining characters in s
                remaining_result = self.helper(s[start_idx:], wordDict, memo) 
                
                # word is what s starts with (or the remaining characters in s start with) up to where remaining result starts
                # join the word and each of the remaining result possibilities together
                for item in remaining_result: 
                    result.append(word + " " + item)
        memo[s] = result
        return result              
                
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
        
        
        
        
        