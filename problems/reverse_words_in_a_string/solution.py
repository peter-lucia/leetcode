class Solution:
    def reverseWords(self, s: str) -> str:
        str_clean = s.strip()
        str_clean = re.sub(" +", " ", str_clean) # + means one or more
        tokens = str_clean.split(" ")
        tokens.reverse() # reverses list of strings in place.
        return " ".join(tokens)
        