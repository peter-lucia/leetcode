class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        {
            elem -> occurrences
        }

        get values
        sort values
        return top k
        """
        lookup = defaultdict(int)
        for num in nums:
            lookup[num] += 1
        
        vals = list(lookup.items())
        vals.sort(key = lambda elem: elem[1], reverse=True)
        vals = vals[:k]
        return [each[0] for each in vals]

