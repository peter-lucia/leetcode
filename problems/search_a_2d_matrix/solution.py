class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        def get_pos(i) -> Tuple[int, int]:
            row = i // m
            col = i - row*m
            return row, col

        low = 0
        high = n*m - 1

        while low <= high:

            mid = low + ((high - low) // 2)
            x,y = get_pos(mid)
            if matrix[x][y] > target:
                high = mid - 1
            elif matrix[x][y] < target:
                low = mid + 1
            else:
                return True
        return False

