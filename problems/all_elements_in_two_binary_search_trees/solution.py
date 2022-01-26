# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        result = []
        
        def dfs(node: TreeNode):
            
            if node is None:
                return
            
            idx = bisect.bisect(result, node.val)
            result.insert(idx, node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root1)
        dfs(root2)
        return result
            
        
        