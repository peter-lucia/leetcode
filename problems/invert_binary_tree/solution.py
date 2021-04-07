# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            if root.left is not None:
                root.left = self.reverse(root.left)

            if root.right is not None:
                root.right = self.reverse(root.right)
        return root
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        return self.reverse(root)
        
        