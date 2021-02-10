class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        d = [[1 for _ in range(cols)] for _ in range(rows)]
        
        for row in range(1, rows):
            for col in range(1, cols):
                d[row][col] = d[row - 1][col] + d[row][col-1]
                
        return d[m-1][n-1]