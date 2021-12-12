class Solution:
     def get_k_words(self, i: int, words: List[str], maxWidth: int) -> int:
        """
        Gets the number of words starting at pos i in the words list that 
        can fit within maxWidth characters with at least one space between them
        """
        k = 0
        n = len(words)
        line = ' '.join(words[i:i+k])
        
        while len(line) <= maxWidth and i+k <= n:
            k += 1
            line = ' '.join(words[i:i+k])
        k -= 1
        return k
    
     def insert_spaces(self, i: int, words: List[str], maxWidth: int, k: int) -> str:
        """
        Returns a line with extra spaces added between the words to fit maxWidth
        """
        
        line = ' '.join(words[i: i+k])
        n = len(words)
        
        # if the line contains only one word or we've reached the last word, 
        # put spaces to the right (i.e. left justify the word)
        if k == 1 or i+k == n:
            spaces = maxWidth - len(line)
            line = line + " " * spaces
        else:
            # Example: 'word1    word2' k = 2, with k-1=1 space between the words 
            spaces = k-1
            total_space_chars = maxWidth - len(line) + spaces
            
            # extra spaces between words should be distributed as evenly as possible
            avg_spaces_between_words = total_space_chars // spaces
            
            # if the number of spaces on a line does not divide evenly between words, 
            # the empty slots on the left will be assigned more spaces than those
            # on the right
            num_words_with_extra_space = total_space_chars % spaces
            if num_words_with_extra_space > 0:
                line = (" " * (avg_spaces_between_words + 1)).join(words[i:i+num_words_with_extra_space])
                line += " " * (avg_spaces_between_words + 1)
                line += (" " * (avg_spaces_between_words)).join(words[i+num_words_with_extra_space:i+k])
            else:
                line = (" " * avg_spaces_between_words).join(words[i:i+k])
        return line       
    
     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # approach
        # Until we have added all words:
        # 1. Get i:i+k words that can fit on a line with maxWidth
        # 2. Insert the spaces between those words
        # 3. Add the line to the result
        
        i = 0
        n = len(words)
        result = []
        
        while i < n:
            k = self.get_k_words(i, words, maxWidth)
            line = self.insert_spaces(i, words, maxWidth, k)
            result.append(line)
            i += k
            
        return result 
    
