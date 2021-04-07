# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:      
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse_tree(current_node):
            
            # if we haven't reached the end of a branch, return false
            if not current_node:
                return False
            
            # left recursion
            left_is_p_or_q = recurse_tree(current_node.left)
            
            # right recursion
            right_is_p_or_q = recurse_tree(current_node.right)
            
            # if current node is either p or q
            current_node_is_p_or_q = current_node == p or current_node == q
            
            if ((current_node_is_p_or_q and left_is_p_or_q) or 
                (current_node_is_p_or_q and right_is_p_or_q) or 
                    (left_is_p_or_q and right_is_p_or_q)):
                self.ans = current_node
            
            return current_node_is_p_or_q or left_is_p_or_q or right_is_p_or_q
        recurse_tree(root)
        return self.ans
        