# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # use dfs with inorder
        result = []
        def dfs(node: TreeNode):
            if node is None:
                return
            
            if node.left:
                dfs(node.left)
                
            result.append(node)
                
            if node.right:
                dfs(node.right)
                
        dfs(root)
        for idx, each in enumerate(result[:-1]):
            each.left = None
            each.right = result[idx+1]
        result[-1].left = None
        return result[0]
            
        