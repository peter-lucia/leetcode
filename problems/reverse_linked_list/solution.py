# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        while head:
            # Store the next node to move the head to later
            head_next = head.next

            # Set the head's next value to the previous value
            head.next = prev

            # Set prev to head
            prev = head
            
            # Move the head forward
            head = head_next

        head = prev
        return prev

            
            