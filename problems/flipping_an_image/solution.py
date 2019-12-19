class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # option 1: reverse each row, append to B
        # invert each bit in B
        # done
        B = A.copy()
        for idx, row in enumerate(A):
            tempRow = row
            tempRow.reverse()
            tempRow = [int(not each) for each in tempRow]
            B[idx] = tempRow
        return B
        
            
            
        