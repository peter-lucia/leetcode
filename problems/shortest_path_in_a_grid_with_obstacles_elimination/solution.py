class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # This is modified BFS
        # Time complexity: O(nk) since each cell could be visited up to k times
        # Space complexity: O(nk) since the queue could potentially house all cells in the grid
        # with every possible value of k
        n = len(grid)
        m = len(grid[0])
        num_steps_to_bottom_edge = n - 1
        num_steps_to_right_edge = m - 1
        manhattan_dist = num_steps_to_bottom_edge + num_steps_to_right_edge
        if manhattan_dist <= k:
            return manhattan_dist
        queue = []
        state = (0,0,k)
        queue.append([state])
        visited = set(state)
        while queue:
            path = queue.pop(0)
            ii, jj, k = path[-1]
            
            if (ii, jj) == (n-1, m-1):
                # with BFS, whichever path gets here first wins
                print("Shortest path = ", *path)
                return len(path) - 1
            
            # visit each neighbor
            for (iii, jjj) in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                if iii < 0 or jjj < 0 or iii >= n or jjj >= m:
                    continue
                    
                new_eliminations = k
                    
                if grid[iii][jjj] == 1:
                    if k > 0:
                        new_eliminations = k - 1
                    else:
                        continue
                        
                new_state = (iii, jjj, new_eliminations)
                new_path = list(path)
                        
                if new_state in visited:
                    continue
                    
                visited.add(new_state)
                new_path.append(new_state)
                queue.append(new_path)
                
            visited.add((ii, jj, k))
            
        return -1
        
        
            
            
        