class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # separate evens and odds in a hash table
        lookup = {}
        for each in A:
            if each % 2 == 0:
                lookup["evens"] = lookup.get("evens", []) + [each]
            else:
                lookup["odds"] = lookup.get("odds", []) + [each]
        # join the evens and odds in a single list with the evens first
        return lookup.get("evens", []) + lookup.get("odds", [])
        