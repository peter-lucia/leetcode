class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []
        for x in range(n+1):
            ans = 0
            while x:
                if x & 1:
                    ans += 1
                x = x >> 1
            result.append(ans)
        return result

