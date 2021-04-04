class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # T[i][j] = size of the largest square edge up to and including indexes i and j
        n = len(matrix)  # given 1 <= n
        m = len(matrix[0])  # given 1 <= m
        
        T = [[0 for _ in range(m)] for _ in range(n)]
       
        mx = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    T[i][j] = min(T[i][j-1], T[i-1][j], T[i-1][j-1]) + 1
                    if T[i][j] > mx:
                        mx = T[i][j]
                else: 
                    T[i][j] = 0
        return mx**2
                