class Solution:
            
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        prevSpot = None
        nextSpot = None
        
        for idx in range(0, len(flowerbed)):
            if idx == 0:
                prevSpot = 0
                if len(flowerbed) > 1:
                    nextSpot = flowerbed[idx+1]
                else:
                    nextSpot = 0
            elif idx == len(flowerbed) - 1:
                nextSpot = 0
                if idx-1 >= 0:
                    prevSpot = flowerbed[idx-1]
                else:
                    prevSpot = 0
            else:
                prevSpot = flowerbed[idx-1]
                nextSpot = flowerbed[idx+1]
                
            if prevSpot == 0 and nextSpot == 0 and flowerbed[idx] != 1:
                flowerbed[idx] = 1
                n -= 1
            
                
        if n > 0:
            return False
        return True
            
                
            
            