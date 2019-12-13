class Solution:
    def removeVowels(self, S: str) -> str:
        result = ""
        for each in S:
            if each not in ["a", "e", "i", "o", "u"]:
                result += each
        return result
                
        