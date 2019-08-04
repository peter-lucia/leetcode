class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0: return result
        if len(strs) == 1: return strs[0]
        
        minLen = sys.maxsize
        for each in strs:
            minLen = len(each) if len(each) < minLen else minLen
                
        low = 1
        high = minLen
        while low <= high:
            mid = int((low + high) / 2)
            if (self.isCommonPrefix(mid, strs)):
                low = mid + 1
            else:
                high = mid - 1
                
        return strs[0][0:int((low+high)/2)]
    
    def isCommonPrefix(self, mid, strs):
        prefix = strs[0][0:mid]
        for each in strs:
            if not each.startswith(prefix):
                return False
        return True
        
            
        
            