class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        # rotate across top left to bottom right diagonal
        for i in range(n):
            for j in range(i, m):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
                
        
        