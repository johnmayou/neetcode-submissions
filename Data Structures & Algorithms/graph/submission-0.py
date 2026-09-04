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
        if src not in self.adj or dst not in self.adj[src]:
            return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        visited = set()

        if src in self.adj:
            q.append(src)
            visited.add(src)

        while q:
            for _ in range(len(q)):
                dest = q.popleft()
                if dest == dst:
                    return True

                for neighbor in self.adj[dest]:
                    q.append(neighbor)
                    visited.add(neighbor)

        return False