# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listNodeToArray(self, listNode):
        result = []
        if listNode is None:
            return result
        while True:
            result.append(listNode.val)
            listNode = listNode.next
            if listNode is None:
                break
        return result
    
    def arrayToListNode(self, arr):
        if not arr:
            return None
        nodes = []
        node = ListNode(arr[0])
        nodes.append(node)
        for num in arr[1:]:
            node.next = ListNode(num)
            node = node.next
            nodes.append(node)
            
        result_length = len(nodes)
        for i in range(0, result_length):
            if i < result_length - 1:
                nodes[i].next = nodes[i+1]
        return nodes[0]

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = int("".join([str(each) for each in self.listNodeToArray(l1)]))
        num2 = int("".join([str(each) for each in self.listNodeToArray(l2)]))
        return self.arrayToListNode([c for c in str(num1 + num2)])
        