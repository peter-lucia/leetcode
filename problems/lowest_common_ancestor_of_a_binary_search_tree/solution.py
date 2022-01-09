# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Use DFS postorder traversal to decide whether p and q
        # are in the left and right subtree of the current node. 
        # the first time we find them both in the left and right
        # subtrees, we return that node, as this will be the lowest
        # common ancestor of p and q.
        # We will need to return whether p or q is the current node
        # or whether p or q are in the left or right subtrees
        # as soon as we find p and q
        # Time complexity: O(V) 
        # Space complexity: O(h) which is the maximum height of the tree
        # This is because we store the height of the tree 
        # in the recursive call stack
        # If the tree is a linked list, this would be O(V)
        
        self.lca = None
        
        def dfs(node: TreeNode):
            if node is None:
                return False, False 
            
            has_p = False
            has_q = False
            
            left_subtree_has_p, left_subtree_has_q = dfs(node.left)
            right_subtree_has_p, right_subtree_has_q = dfs(node.right)
            
            if node.val == p.val:
                has_p = True
            if node.val == q.val:
                has_q = True
                
            has_p = left_subtree_has_p or right_subtree_has_p or has_p
            has_q = left_subtree_has_q or right_subtree_has_q or has_q
                
            if has_p and has_q and self.lca is None:
                self.lca = node
            
            return has_p, has_q
        
        dfs(root)
        return self.lca
               
            
        
        
            
        
        
        
        
        