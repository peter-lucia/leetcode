from typing import List
class Trie:
    def __init__(self, size):
        self.size = size
        self.root = {}
    
    def add_num(self, num: int):
        current = self.root
        for left_shift in range(self.size, -1, -1):
            val = 1 if num & (1 << left_shift) else 0
            if val not in current:
                current[val] = {}
            current = current[val]
        current['end'] = num
                
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Approach: build a trie representing the binary form of all numbers
        # with height equal to the largest number's bit length

        L = len(bin(max(nums))) - 2
        trie = Trie(size=L)
        
        # build trie
        for num in nums:
            trie.add_num(num)
            
        ans = 0
        # for each num, find the number which can create max value with num using XOR
        for num in nums:  
            node = trie.root
            for shift in range(L, -1, -1):
                # verify bit from left to right
                val = 1 if num & (1 << shift) else 0  
                # try opposite bit first, otherwise use same bit
                node = node[1-val] if 1-val in node else node[val] 
            # maintain maximum
            ans = max(ans, num ^ node['end'])            
        return ans    

        