# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode, level=0) -> int:
        if root is None:
            return level
        
        level += 1
        
        if root.left and root.right:
            return max(self.maxDepth(root.left, level=level), self.maxDepth(root.right, level=level))
        elif root.left and not root.right:
            return max(self.maxDepth(root.left, level=level), level)
        elif root.right and not root.left:
            return max(self.maxDepth(root.right, level=level), level)
        return level
            
                       
        