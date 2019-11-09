class Solution(object):
    
    def isHeightFoundLater(self, start_idx, height, arr):
        if start_idx+1 < len(arr):
            for i in range(start_idx+1, len(arr)):
                if arr[i] >= height:
                    return True
        return False
    
    def getMaxHeightFoundLater(self, start_idx, arr):
        if start_idx+1 not in range(0, len(arr)):
            return 0
        
        return max(arr[start_idx+1:])

    def getFirstStepUp(self, height):
        min_height = min(height)
        idx_min_height = height.index(min_height)
        for idx, each in enumerate(height):
            if each > min_height and idx > idx_min_height:
                return each, idx
        return min_height, idx_min_height
                    
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -=1
        return areas