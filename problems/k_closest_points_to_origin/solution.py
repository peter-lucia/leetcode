class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = points.copy()
        n = len(points)
        for i in range(n):
            points[i].append(math.sqrt(points[i][0]**2 + points[i][1]**2))
        points.sort(key=lambda val: val[2]) # increasing
        result = []
        for i in range(k):
            result.append([points[i][0], points[i][1]])
        return result