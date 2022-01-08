# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Approach (DFS)
        # For each tree, get array of values for each node while traversing:
        #   1. preorder
        #   2. inorder
        # If the preorder & inorder vals for the candidate subtree are subarrays
        # of the preorder and inorder vals for the tree, return True, otherwise return False
        # Note: if a node is none, append special character to preorder and inorder value arrays
        #       to prevent a match when the subtree has children in the larger tree
        
        root_vals_inorder = []
        root_vals_preorder = []
        
        subroot_vals_inorder = []
        subroot_vals_preorder = []
        
        
        def dfs(node: TreeNode, vals_preorder: List[int], vals_inorder: List[int]):
            if node is None:
                # prevent match when subtree has children in the larger tree
                vals_preorder.append('#')
                vals_inorder.append('#')
                return
            
            vals_preorder.append(node.val)
            dfs(node.left, vals_preorder, vals_inorder)
            vals_inorder.append(node.val)
            dfs(node.right, vals_preorder, vals_inorder)
        
                
        dfs(root, root_vals_preorder, root_vals_inorder)
        dfs(subRoot, subroot_vals_preorder, subroot_vals_inorder)
        
        root_vals_preorder = "".join(str(each) for each in root_vals_preorder)
        root_vals_inorder = "".join(str(each) for each in root_vals_inorder)
        subroot_vals_preorder = "".join(str(each) for each in subroot_vals_preorder)
        subroot_vals_inorder = "".join(str(each) for each in subroot_vals_inorder)
        
        return (subroot_vals_inorder in root_vals_inorder and 
                subroot_vals_preorder in root_vals_preorder)
        
            
        