class Solution:
    def hammingWeight(self, n: int) -> int:

        result = 0
        while n:
            if 1 & n:
                result += 1
            n = n >> 1
        return result
        