class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Convert to lower
        Extract all alphanumeric characters
        i = 0, j = len(s) - 1
        Verify each increment of i and
        each decrement of j points to the same char
        Stop when i >= j
        """
        s = s.lower()
        valid_chars = set([
            'a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x',
            'y','z','0','1','2','3','4','5',
            '6','7','8','9',
        ])
        p = ""
        for each in s:
            if each in valid_chars:
                p += each
        i = 0
        j = len(p) - 1
        while i < j:
            if p[i] != p[j]:
                return False
            i += 1
            j -= 1
        return True
