class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.level = {}
        self.num_components = n

        for i in range(n + 1):
            self.par[i] = i
            self.level[i] = 0

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]] # path compression
            x = self.par[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.level[px] < self.level[py]:
            self.par[px] = py
            self.level[py] += self.level[px]
        else:
            self.par[py] = px
            self.level[px] += self.level[py]

        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components