class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Key points:
        # we only need to keep multiplying n * 10 and adding 1 until n%k == 0
        # since n might overflow, we need to use the remainder
        # the remainder and n have the same remainder of k, so it's
        # okay to use the remainder instead of n
        # note that if n does not exist, the while loop will continue
        # endlessly, so we find a remainder that repeats, we return -1
        
        remainder = 1
        length_n = 1
        
        seen_remainders = set()
        
        while remainder % k != 0:
            n = remainder*10 + 1
            remainder = n % k
            length_n += 1
            if remainder in seen_remainders:
                return -1
            else:
                seen_remainders.add(remainder)
        return length_n
        