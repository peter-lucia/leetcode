class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Key points:
        # 1. if len(changed) is not even, return []
        
        # approach 2
        # O(nlogn) time complexity at least
        # O(n) space complexity since we just have a hash table of all elements and their num occurrences
        
        # Algorithm
        # 1. put count of each element into a hashmap 
        # 2. iterate over a sorted list of the keys in the hashmap
        # 3. for each key in the sorted list of keys
        #    - add special handling for 0
        #    - if 2*key is another key in the map and it occurs > 0 times, decrement occurrences of key and 2*key
        #    - add key to the result
        #    - once the # of doubles reaches n / 2, return the result
        
        lookup = defaultdict(int)
        
        for each in changed:
            lookup[each] += 1
            
        result = []
        keys = sorted(lookup.keys())
        i = 0
        while i < len(keys):
            each = keys[i]
            if each == 0:
                num_zeros_added = lookup[0] // 2
                result += [0 for _ in range(num_zeros_added)]
                lookup[0] -= num_zeros_added
            elif 2*each in lookup and lookup[2*each] > 0 and lookup[each] > 0:
                num_subtract = min(lookup[2*each], lookup[each])
                lookup[2*each] -= num_subtract
                lookup[each] -= num_subtract
                result += [each for _ in range(num_subtract)]
            i += 1
                
            if len(result) == len(changed) / 2:
                return result
        return []
                
        
        