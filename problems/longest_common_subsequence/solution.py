     
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        if n == 0 or m == 0:
            return 0
        
        T = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
                    
        return T[n][m]
