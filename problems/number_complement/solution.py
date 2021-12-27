class Solution:
    def findComplement(self, num: int) -> int:
        # minimum number of bits needed to represent num in binary
        bit_length = num.bit_length()
        mask = ((1 << bit_length) - 1)
        return num ^ mask