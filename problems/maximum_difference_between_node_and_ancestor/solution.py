# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, root: TreeNode, v: int, max_a: int, min_a: int):
        
        if root is None:
            return v
          
        if root.left is not None:
            _v = max(v, abs(max_a - root.left.val), abs(min_a - root.left.val))
            _max_a = max(max_a, root.left.val)
            _min_a = min(min_a, root.left.val)
            max_left = self.dfs(root.left, _v, _max_a, _min_a)
        if root.right is not None:
            _v = max(v, abs(max_a - root.right.val), abs(min_a - root.right.val))
            _max_a = max(max_a, root.right.val)
            _min_a = min(min_a, root.right.val)
            max_right = self.dfs(root.right, _v, _max_a, _min_a)
        
        if root.left is not None and root.right is not None:
            return max(max_left, max_right)
        if root.left is not None:
            return max_left
        if root.right is not None:
            return max_right
        return v
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Use BFS (level order traversal)
        # Greedy approach: at each level calculate max v
        v = 0
        max_a = root.val
        min_a = root.val
        return self.dfs(root, v, max_a, min_a)
        
        
                