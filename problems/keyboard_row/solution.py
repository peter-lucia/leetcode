class Solution(object):
    def row(self, n):
        top = ['q','w','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        bottom = ['z','x','c','v','b','n','m']
        
        if n in top:
            return 1
        elif n in middle:
            return 2
        elif n in bottom:
            return 3
        else:
            return 0
    
    def findWords(self, words):
        result = []
        for word in words:
            word_l = word.lower()
            prev = self.row(word_l[0])
            out = True
            for i in range(1, len(word_l)):
                if prev != self.row(word_l[i]):
                    out = False
                    break
                else:
                    prev = self.row(word_l[i])            
            if out:
                result.append(word)
        return result