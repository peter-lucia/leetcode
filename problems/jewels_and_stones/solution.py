class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for each in S:
            if each in J:
                total += 1
                
        return total