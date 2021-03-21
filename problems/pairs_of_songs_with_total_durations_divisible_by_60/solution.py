class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        lookup = {}
        counter = 0
        for t in time:
            num_needed = -t % 60
            curr_remainder = t % 60
            if num_needed in lookup:
                counter += lookup[num_needed]
            lookup[curr_remainder] = lookup.get(curr_remainder, 0) + 1
        return counter