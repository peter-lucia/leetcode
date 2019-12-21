class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        if N == 0:
            return a
        for i in range(1,N):
            old_a = a
            a = b
            b = old_a + b
        return b


        