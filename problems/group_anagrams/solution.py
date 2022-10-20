class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {
        #     letters sorted -> words
        # }
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
    
        return lookup.values()
