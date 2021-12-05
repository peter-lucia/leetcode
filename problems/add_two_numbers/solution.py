# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                    
        # if either l1 or l2 is empty, whatever the other list is will be the answer, 
        # even if it's also empty
        if not l1:
            return l2
        if not l2:
            return l1
        
        result = None
        prev = None
        curr = None
        carry = 0
        while l1 or l2:
            if l1 and l2:
                # add val of both nodes together, add carry as well
                new_node = ListNode((carry + l1.val + l2.val) % 10)
                carry = (carry + l1.val + l2.val) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                # only take into consideration the carry and l1's value since l2 is empty
                new_node = ListNode((carry + l1.val) % 10)
                carry = (carry + l1.val) // 10
                l1 = l1.next
            elif not l1 and l2:
                # only take into consideration the carry and l2's value since l1 is empty
                new_node = ListNode((carry + l2.val) % 10)
                carry = (carry + l2.val) // 10
                l2 = l2.next
            # curr points to new node
            # append curr to the result
            curr = new_node
            # if result is empty, curr will be the head. Set the result to the head
            if not result:
                # can't set result = curr because they will point to the same object
                # and the curr will be updated which will also update result
                # adding curr to a list then extracting it out is a workaround
                # This preserves O(1) space complexity
                # With O(n) space complexity, could add all elements to a list
                # then pick out the first one, or any other element in the list
                # kind of defeats the purpose of using linked lists though...
                result = [curr][0]  
            # if prev is not None, set it's next value to the current node
            if prev:
                prev.next = curr
            # move prev and curr forward one node each
            prev = curr
            curr = curr.next
            
        # in case we have a carry at the end,
        # create a new node with the carry's value
        # carry will always be < 10
        if carry > 0:
            new_node = ListNode(carry)
            prev.next = new_node
                      
        return result
            
        