"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return []
        result = [[] for _ in range(1000)]
        queue = []
        queue.append((root, 0))
        
        while queue:
            (elem, level) = queue.pop(0)
            result[level] = result[level] + [elem.val]
            
            for child in elem.children:
                if child is not None:
                    queue.append((child, level + 1))
            
        
        return result[:level+1]
            
            
            
        
        
        
        
        
        
        
        