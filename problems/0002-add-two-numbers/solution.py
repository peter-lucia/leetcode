# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        list1 = list1[::-1]
        list2 = list2[::-1]

        a1 = int("".join([str(each) for each in list1]))
        a2 = int("".join([str(each) for each in list2]))
        result = a1 + a2

        result = [each for each in str(result)] 
        result = result[::-1]

        orig = ListNode(0)
        r = orig
        for c in result:
            r.next = ListNode(int(c))
            r = r.next

        return orig.next
        
