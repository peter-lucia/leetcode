class Solution:
        
            
    def getNextDay(self, cells):
        result = [0]
        for i in range(1, len(cells)-1):
            result.append(int(cells[i-1] == cells[i+1]))
        result.append(0)
        return result

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        fast_forwarded = False
        cache = {}
        while n > 0:
            if not fast_forwarded:
                if tuple(cells) in cache:
                    idx_cells_last_seen = cache[tuple(cells)]
                    cells_since_last_seen = idx_cells_last_seen - n
                    # fast forward by skipping over the cycles until we hit the remainder
                    n %= cells_since_last_seen
                    fast_forwarded = True
                else:
                    cache[tuple(cells)] = n
                
            if n > 0:
                n -= 1
                cells = self.getNextDay(cells)
        
        return cells