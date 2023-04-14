class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)

        vals = sorted([(k, v) for k, v in c.items()], reverse=True, key=lambda val: val[1])
    
        return [first for first, second in vals[:k]]

        


