class Solution:
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        d = set(words)
        
        @functools.cache
        def dfs(word):
            """
            Determine if the word exists in the set of words d
            """
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            return False
        
        result = []
        
        for word in words:
            if dfs(word):
                result.append(word)
        return result
            
        
            
        