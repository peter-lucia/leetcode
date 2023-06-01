# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return None

        result = ListNode()
        head = result
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    head.val = list1.val
                    list1 = list1.next
                else:
                    head.val = list2.val
                    list2 = list2.next
            elif list1:
                head.val = list1.val
                list1 = list1.next
            elif list2:
                head.val = list2.val
                list2 = list2.next
            if list1 or list2:
                head.next = ListNode()
                head = head.next
        return result
