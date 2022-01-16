class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   ''  a  b  c  d  e
        # '' 0  0  0  0  0  0
        # a  0  1  1  1  1  1
        # e  0  1  1  1  1  2
        # c  0  1  1  2  2  2
        # d  0  1  1  1  3  3
        # e  0  1  1  1  3  4


        #   ''  a  b  e  x  q
        # '' 0  0  0  0  0  0
        # a  0  1  1  1  1  1
        # e  0  1  1  2  2  2
        # c  0  1  1  2  2  2
        # d  0  1 `1` 2  2  2   # Remember when text1[i] == text2[j], let dp[ii][jj] = dp[ii-1][jj-1] + 1
        # e  0  1  1  2  2  2
        if len(text1) == 0 or len(text2) == 0:
            return 0
        n = len(text1)
        m = len(text2)

        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                # use i, j for text1 and text2
                # use ii, jj for dp table
                ii = i+1
                jj = j+1
                if text1[i] == text2[j]:
                    dp[ii][jj] = 1 + dp[ii-1][jj-1]
                else:
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
        return dp[n][m]