class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # Observations / Notes

        # Approach # 3
        # Invert the first row
        # for all rows if none equal the first row or its inversion, return False
        # otherwise return True

        # Time complexity: O(nm)
        # Space complexity: O(n)

        r1 = grid[0]
        r1_inv = [int(not elem) for elem in grid[0]]

        for row in grid[1:]:
            if row != r1 and row != r1_inv:
                return False
        return True