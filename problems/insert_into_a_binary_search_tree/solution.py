# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                node = node.right
            elif node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                node = node.left
        return TreeNode(val)
            
        
        