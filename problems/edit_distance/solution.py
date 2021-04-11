class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        if word1 == word2:
            return 0
        n = len(word1)
        m = len(word2)
        T = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            T[i][0] = i
        for j in range(1, m+1):
            T[0][j] = j        

        for i in range(1, n+1):
            for j in range(1, m+1):
                # word[i-1] or word[j-1] converts 1 based index to 0 based index
                # and corresponds to diff at T[i][j]
                diff = 1 if word1[i-1] != word2[j-1] else 0
                T[i][j] = min(T[i-1][j-1] + diff, T[i][j-1] + 1, T[i-1][j] + 1)
                
        return T[n][m]
        
        