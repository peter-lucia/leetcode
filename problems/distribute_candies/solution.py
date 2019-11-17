class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        lookup = {}
        for each in candies:
            lookup[each] = lookup.get(each, 0) + 1
            
        return min(len(lookup), len(candies) // 2)