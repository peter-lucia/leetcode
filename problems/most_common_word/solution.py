class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace('"', " ")
        paragraph = paragraph.replace('`', " ")
        paragraph = paragraph.replace("  ", " ")
        
        banned = set(banned)
        
        words = paragraph.split(" ")
        
        lookup = {}
        for word in words:
            if word not in banned:
                lookup[word] = lookup.get(word, 0) + 1
            
        words_and_usage_count = []
        for word in lookup:
            words_and_usage_count.append((word, lookup[word]))
            
        words_and_usage_count.sort(key=lambda val: val[1], reverse=True) # reverse will be decreasing
        
        return words_and_usage_count[0][0]
            
            
        