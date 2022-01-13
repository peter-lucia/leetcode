class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Approach: add each number to a hashmap num (int) -> occurrences (int)
        # sorted the hashmap by values
        # return the first k keys in the sorted hashmap
        
        lookup = defaultdict(int)
        for num in nums:
            lookup[num] += 1
        
        sorted_lookup = sorted(list(lookup.items()), key=lambda val: val[1], reverse=True)
        result = []
        for i, (key,value) in enumerate(sorted_lookup):
            result.append(key)
            if i+1 == k:
                break
        return result
        