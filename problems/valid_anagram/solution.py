class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for k in s:
            s_dict[k] += 1

        t_dict = defaultdict(int)
        for k in t:
            t_dict[k] += 1
        
        return s_dict == t_dict

