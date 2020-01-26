class Solution:        
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialize the number of islands found to 0
        count = 0
        # for each row in the grid, set i = the index, iv equal to the value
        for i,iv in enumerate(grid):
            # for each column in the current row, j = index of col, jv = value
            for j,jv in enumerate(iv):
                # if the current value of the column is 1, we have found a new island
                if jv == "1":
                    # perform dfs on this island's position, marking all spots on the island as -1
                    # instead of 1 to show that the island is covered for future
                    # iterations
                    self.dfs(grid,i,j)
                    # increase the count of the islands found
                    count += 1

        return count

    def dfs(self,grid: [[str]], i: int, j:int):
        # if i or j are outside the bounds of the grid
        if i >= len(grid) or j >= len(grid[i]):
            return
        # if we have found water instead of an island, or a previously
        # seen spot on an island, return
        if i < 0 or j < 0 or grid[i][j] == "0" or grid[i][j] == "-1":
            return
        
        # otherwise, mark this spot on the island as found
        grid[i][j] = "-1"

        # recursively explore all other adjacent positions (top, down, left, and right)
        # and mark them as found.
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1,j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        