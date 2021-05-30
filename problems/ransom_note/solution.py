class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_lookup = {}
        for letter in magazine:
            mag_lookup[letter] = mag_lookup.get(letter, 0) + 1
        for letter in ransomNote:
            if mag_lookup.get(letter, 0) > 0:
                mag_lookup[letter] -= 1
            else:
                return False
                
        return True 