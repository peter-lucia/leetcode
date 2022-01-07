class Solution:

    def __init__(self, head: Optional[ListNode]):
        ########### Approach 1 O(n) #######################
        # Find the length of the linked list, n, here to get the upper bound

        ########### Approach 2: O(n) #######################
        # Use a hashmap to traverse the linked list once, mapping indexes to each node
        # e.g.
        # 0 -> head
        # 1 -> head.next
        # ...
        # Edge cases: empty list
        self.head = [head][0]
        self.lookup = {}
        self.n = 0
        while head:
            self.lookup[self.n] = [head][0]
            head = head.next
            self.n += 1

    def getRandom(self) -> int:
        ########### Approach 1: O(n) #######################
        # How to generate a random number?
        # choose a random number, called i, between 0 and n - 1 with random.randint
        # and traverse the linekd list i times and return the value

        ########### Approach 2: O(1) #######################
        # pick a random number and return the node mapped by the lookup
        # e.g.
        # return lookup.get(random.randint(0, self.n-1))
        return self.lookup[random.randint(0, self.n-1)].val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()