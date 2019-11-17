class Solution:
    def getArea(self, left, left_pos, right, right_pos):
        h = min(left, right)
        dist = abs(right_pos - left_pos)
        return h*dist
    
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        
        max_area = 0
        
        while left != right:
            
            max_area = max(max_area, self.getArea(height[left], left, height[right], right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area