# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # if we have reached the end of the list, we cannot swap anymore
        if not head or not head.next:
            return head
        
        first_node = head
        second_node = head.next
        
        # recursively swap the rest of the linked list. 
        # first_node will point to the head once that's completed
        first_node.next = self.swapPairs(second_node.next)
        
        # second node points to the first node
        second_node.next = first_node
        
        return second_node