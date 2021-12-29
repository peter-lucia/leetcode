"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Useful data structures for this problem:
        # Since we are always given a perfect binary tree, 
        # we can use a hashmap and BFS (level order traversal) (left -> right) 
        # Hashmap mapping levels to nodes. Nodes are automatically ordered from left to right at each level
        # in the hashmap
        
        #  0 -> 1
        #  1 -> [2,3]
        #  2 -> [4, 5, 6, 7]
        
        lookup = defaultdict(list)
        if not root:
            return root
        
        def bfs(_node: Node):
            queue = []
            queue.append((0, _node))
            while queue:
                level, node = queue.pop(0)
                if queue and queue[0][0] == level:
                    node.next = queue[0][1]
                # at each level, nodes are always processed from left to right
                if node.left:
                    queue.append((level + 1, node.left))
                if node.right:
                    queue.append((level + 1, node.right))
            
        bfs(root)
        return root
            
            
        
        
        