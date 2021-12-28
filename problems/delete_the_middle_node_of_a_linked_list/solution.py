# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None
    
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        prev_node = nodes[len(nodes) // 2 - 1]
        middle_node = nodes[len(nodes) // 2]
        if len(nodes) // 2 + 1 < len(nodes):
            next_node = nodes[len(nodes) // 2 + 1]
        else:
            next_node = None
        prev_node.next = next_node
        return nodes[0]
        
            
        