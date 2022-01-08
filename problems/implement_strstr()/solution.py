class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        function RabinKarp(string s[1..n], string pattern[1..m])
            hpattern := hash(pattern[1..m]);
            for i from 1 to n-m+1
                hs := hash(s[i..i+m-1])
                if hs = hpattern
                    if s[i..i+m-1] = pattern[1..m]
                        return i
            return not found
        
        Use a rolling hash to construct the substring of the haystack
        s[i+1..i+m] = s[i..i+m-1] - s[i] + s[i+m]
        Source: https://en.wikipedia.org/wiki/Rabin–Karp_algorithm
        """
        
        def hash(s: str) -> int:
            result = 0
            for c in s:
                result += ord(c) % 2069
            return result
        
        
        n = len(haystack)
        m = len(needle)
        
        if n < m:
            return -1
        
        if n == m == 0:
            return 0
        
        hashed_needle = hash(needle)
        
        substr = None
        for i in range(len(haystack)):
            if substr is None:
                substr = haystack[i:i+m]
                hashed_substr = hash(substr)
            elif i+m-1 < n:
                # implements a rolling hash
                # - The earliest hashed character is at i-1 since i was incremented after
                # the previous loop 
                # the next character we want to add to the hash is at i-1+m
                hashed_substr = hashed_substr - hash(haystack[i-1]) + hash(haystack[i-1+m])
                # hashed_substr = hash(haystack[i:i+m])
            else:
                break
                
            if hashed_substr == hashed_needle:
                # verify order is correct since hash doesn't check order
                if needle == haystack[i:i+m]:
                    return i
        return -1
            
            