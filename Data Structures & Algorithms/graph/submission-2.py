class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj:
            return False
        if dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def dfs(cur: int) -> bool:
            if cur == dst:
                return True
            if cur in visited:
                return False

            visited.add(cur)
            for nxt in self.adj[cur]:
                if dfs(nxt):
                    return True

            return False

        return dfs(src)