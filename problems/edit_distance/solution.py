class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        """
        Time complexity: O(nm)
        Space compleity: O(nm)
        """
        n = len(str1)
        m = len(str2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):

                # when first string is empty, only option is to insert
                # all of the characters up to j: requires j operations
                if i == 0:
                    dp[i][j] = j

                # if second string is empty, only option is to insert
                # all of the characters up to i: requires i operations
                elif j == 0:
                    dp[i][j] = i

                # if last characters are the same in str1 and str2,
                # we carry over min operations needed without
                # including the last characters
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # last two characters are different, add an operation
                # to the minimal previous number of operations possible
                # prior to reaching this cell in the dp table
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],  # without last char in str2
                                       dp[i-1][j],  # without last char in str1
                                       dp[i-1][j-1])  # without either chars in str1 and str2
        return dp[n][m]
