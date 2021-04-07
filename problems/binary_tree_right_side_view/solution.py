# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        visited = set()
        queue = deque([])
        result = []
        def bfs(root: TreeNode):
            visited.add(root)
            queue.append((root, 0))
            while queue:
                node, level = queue.popleft()
                if len(result) == level:
                    result.append(node.val)
                # visit to the right first to ensure level equals the right node
                for neighbor in (node.right, node.left):
                     if neighbor is not None:
                            visited.add(neighbor)
                            queue.append((neighbor, level + 1))
                    
                    
                        
        bfs(root)
        return result