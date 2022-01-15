# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Approach
        # Use DFS postorder to find all the leaves
        # Add parent to DFS call so a node can be deleted
        # Add whether the direction is left or right so we know
        # which child node to delete from the parent by setting it to None
        # Wait to delete until after a full traversal
        
        def dfs(node: TreeNode, parent, is_left):
            
            result = []
            
            if node.left:
                 result += dfs(node.left, node, True)
                
            if node.right:
                result += dfs(node.right, node, False)
            
            if node.left is None and node.right is None:
                result.append((node, parent, is_left))
                    
            return result
        
        all_leaves = []
        while root.left is not None or root.right is not None:
            nodes_to_delete = dfs(root, None, False)
            leaves = [node.val for (node, parent, is_left) in nodes_to_delete]  
            all_leaves.append(leaves)
            for (node, parent, is_left) in nodes_to_delete:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
        all_leaves.append([root.val])  
                
        return all_leaves
                
            
            
            
            
        
        
        
        
        
        