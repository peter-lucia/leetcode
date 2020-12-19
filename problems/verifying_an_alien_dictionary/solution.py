class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        lookup = {}
        
        for i, letter in enumerate(order):
            lookup[letter] = alphabet[i]
        
        translated_words = []
        for word in words:
            new_word = ""
            for letter in word:
                new_word += lookup[letter]
            translated_words.append(new_word)
        
        translated_words_2 = sorted(translated_words)
        
        return translated_words == translated_words_2
    