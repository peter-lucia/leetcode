class Solution:
    
    def __init__(self):
        self.rotten = 2
        self.empty = 0
        self.fresh = 1
    
    def isRottenAdjacent(self, grid, x, y):
        positions_to_check = {
            0:[x-1, y],
            1:[x+1, y],
            2:[x, y-1],
            3:[x, y+1]
        }
        
        if x == 0:
            positions_to_check.pop(0)
        if x == len(grid) - 1:
            positions_to_check.pop(1)
        if y == 0:
            positions_to_check.pop(2)
        if y == len(grid[0]) - 1:
            positions_to_check.pop(3)
            
        for key, value in positions_to_check.items():
            x1, y1 = value[0], value[1]
            if x1 < len(grid) and y1 < len(grid[0]):
                if grid[x1][y1] == self.rotten:
                    return True
        return False

    def makePositionsRotten(self, grid, positions):
        grid = copy.deepcopy(grid)
        for each in positions:
            x = each[0]
            y = each[1]
            grid[x][y] = self.rotten
        return grid
    
    def areGridsEqual(self, grid1, grid2):
        """
        Assumes grids are the same shape
        """
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if len(grid1) > i and len(grid1[0]) > j:
                    if grid1[i][j] != grid2[i][j]:
                        return False
                
        return True
    
    def hasOrangeType(self, grid, orange_type):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == orange_type:
                    return True
        return False
                    
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # try to make all oranges rotten,
        # if any orange is not rotten after a sweep, then it's not possible
        # keep track of how many minutes have elapsed
        
        if not self.hasOrangeType(grid, self.fresh):
            return 0
        if not self.hasOrangeType(grid, self.rotten):
            return -1
        
        # grid = copy.deepcopy(grid)
        grid = grid.copy()
        
        minutes = 0
        while True:
            positions_to_rotten = []
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if self.isRottenAdjacent(grid, x, y) and grid[x][y] != self.empty:
                        positions_to_rotten.append([x,y])
            new_grid = self.makePositionsRotten(grid, positions_to_rotten)
            if not self.areGridsEqual(new_grid, grid):
                minutes += 1
                grid = new_grid
            else:
                if minutes == 0:
                    return -1
                if self.hasOrangeType(new_grid, self.fresh):
                    return -1
                break
        return minutes
