# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Approach
        
        nodes = []
        
        if not head:
            return None
        
        while head:
            nodes.append(head)
            head = head.next
            
        return nodes[len(nodes) // 2]
        