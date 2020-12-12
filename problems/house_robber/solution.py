class Solution:
    def rob(self, p: List[int]) -> int:
        n = len(p)

        if n == 0:
            return 0

        T = [0 for _ in range(n)]
        
        T[0] = p[0]
        
        if n > 1:
            T[1] = max(T[0], p[1])
        else:
            return T[0]

        for i in range(2, n):
            T[i] = max(p[i], T[i-1], T[i-2] + p[i])

        return T[n-1]

        