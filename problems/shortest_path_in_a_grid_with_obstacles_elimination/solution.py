class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # Use BFS
        # add state (i, j, k) to queue
        # keep track of visited states
        # don't visit nodes with state k <= 0
        
        n = len(grid)
        m = len(grid[0])
        visited = set()
        queue = []
        queue.append([(0, 0, k)])
        
        # get manhattan distance
        # if manhattan distance <= k, return it
        if n-1 + m-1 <= k:
            return n-1 + m-1
        
        while queue:
            path = queue.pop(0)
            i, j, _k = path[-1]
            
            visited.add((i, j, _k))
            
            if i == n-1 and j == m-1:
                print(*path)
                return len(path) - 1
            
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (x,y) in neighbors:
                if 0 <= x < n and 0 <= y < m:
                    
                    if grid[x][y] == 1:
                        new_k = _k - 1
                        if new_k < 0:
                            continue
                    else:
                        new_k = _k
                    
                    if (x, y, new_k) in visited:
                        continue
                        
                    new_path = list(path)
                        
                    new_path.append((x, y, new_k))
                    visited.add((x, y, new_k))
                    queue.append(new_path)
        return -1
                    
            
            
            
        