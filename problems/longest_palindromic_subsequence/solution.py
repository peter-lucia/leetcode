class Solution:
    def longestPalindromeSubseq(self, x: str) -> int:
        """
        Returns the length of the longest palindromic subsequence

        @param x: a string
        @return: The length of the longest palindromic subsequence
        """

        x = [each for each in x]
        n = len(x)
        y = [x[i] for i in range(n-1, -1, -1)]

        T = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n):
            T[i][0] = 0
        for j in range(n):
            T[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])

        return T[n][n]


        