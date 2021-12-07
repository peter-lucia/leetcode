class Solution:           
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        def dfs(grid: List[List[str]], i, j, visited: List[List[int]]):

            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1' or visited[i][j]:
                return

            visited[i][j] = True 

            dfs(grid, i+1, j, visited)
            dfs(grid, i-1, j, visited)
            dfs(grid, i, j-1, visited)
            dfs(grid, i, j+1, visited)
        
        num_islands = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(grid, i, j, visited)
                    num_islands += 1
        return num_islands

