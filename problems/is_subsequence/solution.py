class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = [each for each in s]
        if len(s) == 0:
            return True
        elif len(s) > 0:
            for idx, each in enumerate(t):
                if each == s[0]:
                    s.pop(0)
                if len(s) == 0:
                    return True
        return False