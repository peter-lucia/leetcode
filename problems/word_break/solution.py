class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        # can use words inf times, so just get the set of them
        word_set = set(wordDict)
        T = [False for _ in range(n+1)]
        # empty string is always true
        T[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if T[j] and s[j:i] in word_set:
                    T[i] = True
        return T[n]
        
                    
                