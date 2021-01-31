class Solution:
    
    def get_next_element(self, i, j, matrix, max_i, max_j, visited, direction="right"):
        """
        Gets the next element and tells the caller which direction to go toward next
        """
        if direction == "right":
            if j < max_j and (i, j+1) not in visited:
                return matrix[i][j+1], "right"
            direction = "down"
        if direction == "down":
            if i < max_i and (i+1, j) not in visited:
                return matrix[i+1][j], "down"
            direction = "left"
        if direction == "left":
            if j > 0 and (i, j-1) not in visited:
                return matrix[i][j-1], "left"
            direction = "up"
        if direction == "up":
            if i > 0 and (i-1, j) not in visited:
                return matrix[i-1][j], "up"
            direction = "right"
            
        return None, direction
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i = 0
        j = 0
        max_i = len(matrix) - 1
        max_j = len(matrix[0]) - 1
        item = matrix[i][j]
        result = []
        result.append(item)
        direction = "right"
        visited = set()
        num_elements = (max_i+1) * (max_j+1)
        while len(visited) < num_elements:
            item, direction = self.get_next_element(i,j, matrix, max_i, max_j, visited, direction=direction)
            visited.add((i,j))
            if len(visited) == num_elements:
                break
            if item is not None:
                result.append(item)
                if direction == "right":
                    j += 1
                elif direction == "down":
                    i += 1
                elif direction == "left":
                    j -= 1
                elif direction == "up":
                    i -= 1
               
        return result