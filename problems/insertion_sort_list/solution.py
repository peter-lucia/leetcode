# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Insertion sort
        # for each node, while it's greater than the previous node swap it (right) with the previous node
        # head  5, 1, 3, 2 
        # result
        
        # head 1, 3, 2       head  3, 2     head  2            head      
        # result 5           result 1, 5    result 1, 3, 5     result 1, 2, 3, 5
        
        result = ListNode()
        curr = head
        
        while curr:
            
            prev = result
            
            # iterate over the resultant linked list and
            # find the first position to insert the node there 
            # where the current node is greater
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            tmp = curr.next
            
            # insert the current node into the resultant linked list between prev and prev.next
            # point prev -> curr -> prev.next
            curr.next = prev.next
            prev.next = curr
            
            curr = tmp
        
        return result.next
            
            