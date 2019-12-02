class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2*cheeseSlices) / 2
        y = cheeseSlices - x
        
        return [int(x),int(y)] if tomatoSlices % 2 == 0 and cheeseSlices * 2 <= tomatoSlices <= cheeseSlices*4 else []