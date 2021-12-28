class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # Approach DFS
        # Run DFS from each vertex if that vertex is not yet visited
        
        num_vertices = len(isConnected)
        
        def dfs(starting_vertex: int, adj_matrix: List[List[int]], visited: set):
            
            visited.add(starting_vertex)
            
            for i in range(len(adj_matrix)):
                if i in visited:
                    continue
                if adj_matrix[starting_vertex][i] == 1:
                    visited.add(i)
                    dfs(i, adj_matrix, visited)
            
        
        cc = 0
        visited = set([])
        for i in range(num_vertices):
            if i not in visited:
                dfs(i, isConnected, visited)
                cc += 1
        return cc
        
            
            
            