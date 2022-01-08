# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach
        # Move list1 head and list2 head through both linked lists
        # If list11 head is less than list2's head, add list1's head to the result
        # repeat until we've traversed both lists
        
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        if list1.val < list2.val:
            head = list1
        else:
            head = list2 
        starting_head = [head][0]
        while list1 or list2:
            
            if list1 and list2:
                if list1.val < list2.val:
                    new_node = list1
                    list1 = list1.next
                else:
                    new_node = list2
                    list2 = list2.next
            elif list1:
                new_node = list1
                list1 = list1.next
            elif list2:
                new_node = list2
                list2 = list2.next
                
            head.next = new_node
            head = head.next
            
        return starting_head
        