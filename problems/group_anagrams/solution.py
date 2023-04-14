class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {
        #     letters sorted -> words
        # }
        lookup = defaultdict(list)
        for word in strs:
            word_sorted = "".join(sorted(word))
            lookup[word_sorted].append(word)
        
        return [v for k, v in lookup.items()]


