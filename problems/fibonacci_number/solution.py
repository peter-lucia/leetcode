class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        T = [0 for _ in range(N+1)]
        T[0] = 0
        T[1] = 1
        for i in range(2, N+1):
            T[i] = T[i-1] + T[i-2]
        return T[N]
            
        