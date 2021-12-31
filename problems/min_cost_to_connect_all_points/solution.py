class DisjointSet:

    def __init__(self, points):
        # Initially the rank (height of tree) for each node is zero 
        # since all nodes are separated
        self.rank = {}
        # Map the node (index) to its parent node. 
        # Initially all nodes are separated, so the parent is itself
        self.parent = {}
        for point in points:
            x, y = point[0], point[1]
            self.parent[(x, y)] = (x,y)
            self.rank[(x,y)] = 0

    def find(self, x: Tuple[int, int]) -> Tuple[int, int]:
        """
        Gets the root node of x
        """
        if x != self.parent[x]:
            x = self.find(self.parent[x])
        return x

    def union(self, x: Tuple[int, int], y: Tuple[int, int]):
        """
        Merges sets that x and y reside in
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            # make root_y have the higher rank if they are equal
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
        
class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build a complete graph connecting all points
        # find the MST
        
        # Build list of edges connecting all points
        edges = []
        for point1 in points:
            for point2 in points:
                if point1 == point2:
                    continue
                x1 = point1[0]
                y1 = point1[1]
                x2 = point2[0]
                y2 = point2[1]
                weight = abs(x2 - x1) + abs(y2 - y1)
                # since all points are distinct, we use the points index in points as its unique identifier
                # This is easier to work with in the disjoint set structure
                edges.append((tuple(point1), tuple(point2), weight))
                
        # Kruskal's algorithm
        # Initially all points are disconnected
        dj_set = DisjointSet(points)
        # sort edges in place by weight, increasing
        edges.sort(key=lambda val: val[2])
        edges_sum = 0
        num_edges = 0
        for (x, y, weight) in edges:
            if dj_set.find(x) != dj_set.find(y):
                edges_sum += weight
                dj_set.union(x, y)
                num_edges += 1
            if num_edges == len(points) - 1:
                # We've built the MST already
                return edges_sum
                
        return edges_sum
        
            