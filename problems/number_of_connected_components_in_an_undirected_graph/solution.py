class Solution:
    
    
    def __init__(self):
        self.adj_list = {}
        
    def explore(self, z: int, adj_list: dict, visited: dict, cc: int, ccnum: dict) -> None:
        visited[z] = True
        ccnum[z] = cc
        if z in adj_list: 
            for w in adj_list[z]:
                if not visited[w]:
                    self.explore(w, adj_list, visited, cc, ccnum)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        n is the number of nodes
        edges are the edges between nodes
        
        Note that some nodes may not have any edges
        """
        
        V = set()
        adj_list = {}
        
        # min vertex value is 0, so mx will always be lower than the lowest vertex
        mx = -1 
        # construct the adjacency list
        # since we're dealing 
        for z, w in edges:
            # undirected graph will require bidirectional paths in the adj list for a single edge
            adj_list[z] = adj_list.get(z, []) + [w]
            adj_list[w] = adj_list.get(w, []) + [z]
            # add nodes to list of vertices
            V.add(z)
            V.add(w)
            # keep track of max vertex value found
            mx = max(max(z, w), mx)
            
        # add nodes that have no edges to them
        additional_nodes = n - len(V) 
        # add any new additional nodes starting with max vertex + 1
        for node in range(mx+1, mx+1+additional_nodes):
            adj_list[node] = {}
            V.add(node)
            
        # run DFS
        cc = 0
        ccnum = {}
        visited = {}
        for v in V:
            visited[v] = False
        for v in V:
            if not visited[v]:
                cc += 1
                self.explore(v, adj_list, visited, cc, ccnum)
        return cc
        