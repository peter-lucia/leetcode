class Solution:
    def longestPalindrome(self, x: str) -> str:
        n = len(x)
        if n == 0:
            return ""
        if n == 1:
            return x
        
        T = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            T[i][i] = 1
        
        imax = 0
        jmax = 0
        mx = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if x[i] == x[j] and (T[i+1][j-1] > 0 or abs(i-j) == 1):
                    T[i][j] = 2 + T[i+1][j-1]
                    if T[i][j] > mx:
                        mx = T[i][j]
                        imax = i
                        jmax = j

        result = ""
        while jmax >= 0 and imax < n and mx > 0:
            result += x[jmax]
            jmax = jmax - 1
            imax = imax + 1
            mx = mx - 1

        return result