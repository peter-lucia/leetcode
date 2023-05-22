class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # get the bit value at position i in n
            bit = (n >> i) & 1
            # get its position in the result
            j = 31 - i
            # get its actual value after shifted to its new position
            val = bit << j
            # add it to the result
            ans +=val
        return ans



