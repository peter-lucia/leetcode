class Solution:
                
    def is_word_in_s(self, word: str, s: str) -> bool:
        for c in word:
            idx = s.find(c)
            if idx == -1:
                return False
            
            s = s[idx+1:]
        return True
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Approach
        
        # Time complexity: O(nklogk) where k is the length of the longest word, n is the number of words
        # Space complexity: O(1) since we just keep a counter of the total number of matches
        # 1. Iterate over each word
        # 2. iterate over each character c in the word
        # 3. if we find c in the word, let s = s[idx_of_c+1:]
        #    otherwise, reject this word
        # 4. if we find all characters of word in s, increment total counter
        # 5. return the counter
        
        result = 0
        for word in words:
            if self.is_word_in_s(word, s):
                result += 1
        return result
                
                    
                
            
            
        
        