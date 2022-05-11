class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = "aeiou"
        return len(list(itertools.combinations_with_replacement(vowels, n)))
        