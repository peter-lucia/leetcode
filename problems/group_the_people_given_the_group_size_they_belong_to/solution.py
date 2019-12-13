class Solution:
    def getChunks(self, items, size):
        result = []
        for i in range(0, len(items), size):
            result.append(items[i:i+size])
        return result
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        
        for idx, each in enumerate(groupSizes):
            groups[each] = groups.get(each, []) + [idx]
            
        result = []
        for key in groups:
            if len(groups[key]) != key:
                result += self.getChunks(groups[key], key)
            else:
                result.append(groups[key])
        return result
                
            
        
        