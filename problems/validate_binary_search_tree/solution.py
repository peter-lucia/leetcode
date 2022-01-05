# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Approach
        
        # Use postorder traversal DFS
        # For each node:
        # Determine if the max value in the left subtree is > node.val
        # Determine if the min value in the right subtree is < node.val
        # If this is true for all nodes, return True, otherwise return False
        
        self.prev = -math.inf
        
        def dfs(node: TreeNode):
            if node is None:
                return True
            
            if not dfs(node.left):
                return False
            
            if self.prev >= node.val:
                return False
            
            self.prev = node.val
            
            if not dfs(node.right):
                return False
            
            return True
        
        return dfs(root)
        
        
        
