# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        # Observations
        
        # If we get back a score of 0, eliminate all words that share > 0 letter positions in common with the last guessed word
        # If we get back a score of 6, have our answer
        # If we get back a score of 1-5, the correct word will have the same number of letter positions in common with the
        # last guessed word as what was returned as the score.
        
        # Approach
        
        # 1. Make a function that filters the wordslist by the words that have
        # at least x number of exact value and position matches as the input word
        
        # 2. Guess a random word from the wordlist
        
        def get_matches(word1: str, word2: str) -> bool:
            # len(word1) == len(word2) since all words are of length 6
            n = len(word1)  
            
            result = 0
            for i in range(n):
                if word1[i] == word2[i]:
                    result += 1
            return result
        
        random.seed(100)
        
        for _ in range(10):
            guess = wordlist[random.randint(0, len(wordlist) - 1)]
            score = master.guess(guess)
            
            if score == 6:
                return guess
            
            i = 0
            while i < len(wordlist):
                matches = get_matches(guess, wordlist[i])
                if score == 0 and matches > 0:
                    wordlist.pop(i)
                elif 0 < score < 6 and matches != score:
                    wordlist.pop(i)
                else:
                    i += 1   
            
                    
        