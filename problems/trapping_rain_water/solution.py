class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        left = 0
        right = len(height) - 1
        
        total = 0
        left_max = 0
        right_max = 0
        while left != right:
            # check if left block is less than right block
            if height[left] < height[right]:
                
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # if left block 
                    total += left_max - height[left]
                
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                
                    total += right_max - height[right]
                right -= 1
        return total
            
            
            
            