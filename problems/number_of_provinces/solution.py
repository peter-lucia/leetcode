class Solution:
    def dfs(self, isConnected, i: int, visited):

        n = len(isConnected)
        m = len(isConnected[0])
        
        for j in range(m):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(isConnected, j, visited)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])

        visited = [0 for _ in range(n)]

        cc = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(isConnected, i, visited)
                cc += 1
        return cc

