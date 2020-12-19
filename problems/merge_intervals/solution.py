class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key=operator.itemgetter(0))

        result = []
        
        for i in range(n):
            if result:
                if (intervals[i][0] <= result[-1][1]):
                    result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]
                else:
                    result.append([intervals[i][0], intervals[i][1]])
            else:
                result.append([intervals[i][0], intervals[i][1]])
        return result
            
        
        