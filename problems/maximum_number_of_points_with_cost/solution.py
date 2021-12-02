class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # approach 1 (seems like this implies approach 2 when you get into the details)
        
        # greedily select numbers with greatest sum at each row
        # iterate through each row
        # find max total sum accounting for sum from previous row
        # and accounting for the subtraction of abs(c1 - c2)
        
        # Time complexity: O(mn) for an m x n matrix since we have to iterate over all elements of the matrix once
        # Space complexity: O(1) since we just need to keep track of the max possible sum
        
        
        # approach 2
        
        # construct a table that contains the max possible sum for the table
        # up to and before coordinates (r,c)
        
        #  for 
        #  1  2  3
        #  1  5  1
        #  3  1  1
        
        # this would look like
        
        
        #  1  2  3
        #  2  7  4 
        #  
        
        # max_sum(1,0) = max{2, 3 - 1, 4 - 2} = max{2, 2, 2} = 2
        # max_sum(1,1) = max{6 - 1, 7, 8 - 1} = max{5, 7, 7} = 7
        # max_sum(1,2) = max{4, 3-1, 2 - 2} = 4
        # max_sum(2,0) = max{4, 8-1, 4, -2} = 7
        
        # base_case 
        # max_sum[i,j] = 0 for all i in 0..n+1 and j in 0..m+1
        
        # recurrence:
        # max_sum(i,j) = max{max_sum[i,j], max_sum[i-1][k] + table[i][j] - (k-j) for all k} where k is between 0 and m
        # and 0 < i < n and 0 < j < m
        
        # Time complexity: O(nm) since we iterate over the entire table once and over m twice
        # Space complexity: O(nm) for the table
        if not points:
            return 0
        n = len(points)
        m = len(points[0])
        max_sum = copy.deepcopy(points)
        
        for i in range(n):
            
            for j in range(m):
                if i > 0:
                    max_sum[i][j] = max(max_sum[i][j], max_sum[i-1][j] + points[i][j])
            for j in range(m-2, -1, -1):
                max_sum[i][j] = max(max_sum[i][j], max_sum[i][j + 1] - 1)
            for j in range(1, m):
                max_sum[i][j] = max(max_sum[i][j], max_sum[i][j - 1] - 1)
        
        # the answer is the max value of the last row
        return max(max_sum[-1])

        
        
        
        
        
        
        
        
        