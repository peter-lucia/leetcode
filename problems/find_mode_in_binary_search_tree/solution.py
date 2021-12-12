# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # binary search tree has the following property:
        # left_subtree (keys) ≤ node (key) < right_subtree (keys)
        # or
        # left_subtree (keys) < node (key) ≤ right_subtree (keys)
        
        # Approach:
        # use BFS to traverse the tree
        # push all elements in the tree into a lookup
        # {
        #     val: num_elements 
        # }
        # find the max occurrences and then all nodes that have the max # occurrences
        lookup = defaultdict(int)
        
        def bfs(node: TreeNode):
            
            if not root:
                return
            
            queue = []
            queue.append(node)
            
            while queue:
                
                elem = queue.pop(0)
                
                lookup[elem.val] += 1
                
                if elem.left is not None:
                    queue.append(elem.left)
                
                if elem.right is not None:
                    queue.append(elem.right)
                
        bfs(root) 
        max_occurrences = max(lookup.values())
        result = []
        for (val, occurrences) in lookup.items():
            if occurrences == max_occurrences:
                result.append(val)
            
        return result
        
                
                
        