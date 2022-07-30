class Solution:
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # let d contain the max count of each possible character found
        # in all of words2
        # for each word in words1, get the counts of each character
        # if the counts of each character are less than the max
        # count for that character among all of words2, don't add that
        # word to the result
        # otherwise, do add that word to the result
        d = {}
        for w2 in words2:
            c = Counter(w2)
            for k, v in c.items():
                if v > d.get(k, 0):
                    d[k] = v
                    
        result = []
        
        for w1 in words1:
            c = Counter(w1)
            can_add = True
            for k, v in d.items():
                if c.get(k, 0) < v:
                    can_add = False
            if can_add:
                result.append(w1)
        
        return result 
                    
                    