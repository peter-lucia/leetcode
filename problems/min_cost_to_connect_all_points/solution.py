class DisjointSet:

    def __init__(self, size: int):
        # Initially the rank (height of tree) for each node is zero 
        # since all nodes are separated
        self.rank = [0 for _ in range(size)]
        # Map the node (index) to its parent node. 
        # Initially all nodes are separated, so the parent is itself
        self.parent = [i for i in range(size)]

    def find(self, x: int) -> int:
        """
        Gets the root node of x
        """
        if x != self.parent[x]:
            x = self.find(self.parent[x])
        return x

    def union(self, x: int, y: int):
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
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                weight = abs(x2 - x1) + abs(y2 - y1)
                # since all points are distinct, we use the points index in points as its unique identifier
                # This is easier to work with in the disjoint set structure
                edges.append((i, j, weight))
                
        # Kruskal's algorithm
        # Initially all points are disconnected
        dj_set = DisjointSet(size = len(edges))
        # sort edges in place by weight, increasing
        edges.sort(key=lambda val: val[2])
        edges_sum = 0
        num_edges = 0
        for (i, j, weight) in edges:
            if dj_set.find(i) != dj_set.find(j):
                edges_sum += weight
                dj_set.union(i, j)
                num_edges += 1
            if num_edges == len(points) - 1:
                # We've built the MST already
                return edges_sum
                
        return edges_sum
        
            