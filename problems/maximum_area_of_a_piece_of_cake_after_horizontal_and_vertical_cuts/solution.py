class Solution:
    
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
            
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        # ensure horizontal and vertical cuts are sorted in increasing order
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hcuts_len = len(horizontalCuts)
        vcuts_len = len(verticalCuts)
        
        max_diff_h = 0
        for i in range(1, hcuts_len):
            max_diff_h = max(max_diff_h, horizontalCuts[i] - horizontalCuts[i-1])
            
        max_diff_v = 0    
        for j in range(1, vcuts_len):
            max_diff_v = max(max_diff_v, verticalCuts[j] - verticalCuts[j-1])
        
        max_possible_area = 10**9+7
        return max_diff_h*max_diff_v % (max_possible_area)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        