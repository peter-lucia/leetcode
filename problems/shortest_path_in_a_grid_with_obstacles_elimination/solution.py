class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # Use BFS
        # Put positional + current k into queue: (i,j, _k)
        n = len(grid)
        m = len(grid[0])
        
        
        # If manhattan distance <= k, just return it
        # since we can go through all obstacles without surpassing k
        if n-1 + m-1 <= k:
            return n-1 + m-1
        
        visited = set()
        queue = deque()
        queue.append([(0,0,k)])
        
        while queue:
            
            path = queue.popleft()
            (i,j,_k) = path[-1]
            
            if i == n-1 and j == m-1:
                print(*path)
                return len(path) - 1
            
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            
            for (ii, jj) in neighbors:
                if not (0 <= ii < n and 0 <= jj < m):
                    continue
                    
                    
                if grid[ii][jj] == 1:
                    if _k > 0:
                        k_new = _k - 1
                    else:
                        continue
                else:
                    k_new = _k
                    
                if (ii, jj, k_new) in visited:
                    continue      
                    
                new_pos = (ii, jj, k_new)
                new_path = list(path)
                visited.add(new_pos)
                new_path.append(new_pos)       
                queue.append(new_path)
                
        
        return -1