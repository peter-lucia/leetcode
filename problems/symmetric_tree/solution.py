# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def is_mirror(self, node1: TreeNode, node2: TreeNode) -> bool:
        
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.val == node2.val and 
                self.is_mirror(node1.left, node2.right) and
                   self.is_mirror(node1.right, node2.left))
            
        
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.is_mirror(root.left, root.right)
        