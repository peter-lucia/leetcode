# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Use DFS postorder, dfs has two return types, has_p, has_q 
        # as soon as both are true, return the current node
                
        self.lca = None     
        def dfs(node: TreeNode, has_p, has_q) -> Tuple[bool, bool]:
            if node is None:
                return has_p, has_q
            
                
            left_has_p, left_has_q = dfs(node.left, has_p, has_q)
            right_has_p, right_has_q = dfs(node.right, has_p, has_q)
            
            if node.val == p.val:
                has_p |= 1
            if node.val == q.val:
                has_q |= 1
                
            has_p |= left_has_p | right_has_p
            has_q |= left_has_q | right_has_q
            
            if has_p == 1 and has_q == 1 and self.lca is None:
                self.lca = node
            
            return has_p, has_q
            
        dfs(root, 0, 0)
        return self.lca
        
        
        
        
        