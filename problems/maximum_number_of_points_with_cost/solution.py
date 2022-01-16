class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Time complexity: O(nm) since we iterate over the entire table once and over m twice
        # Space complexity: O(nm) for the table
        if not points:
            return 0
        n = len(points)
        m = len(points[0])
        max_sum = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    max_sum[i][j] = points[i][j]
                if i > 0:
                    # max sum of points directly above each other
                    max_sum[i][j] = max(max_sum[i][j], max_sum[i-1][j] + points[i][j])
            # get max sum from current row will be available to the next row
            # each move left subtracts 1 from the max sum possible found so far
            # move right -> left
            for j in range(m-2, -1, -1):
                max_sum[i][j] = max(max_sum[i][j], max_sum[i][j + 1] - 1)
            # get max sum from current row will be available to the next row
            # each move right subtracts 1 from the max sum possible found so far
            # move left -> right
            for j in range(1, m):
                max_sum[i][j] = max(max_sum[i][j], max_sum[i][j - 1] - 1)
        # the answer is the max value of the last row
        return max(max_sum[-1])
        