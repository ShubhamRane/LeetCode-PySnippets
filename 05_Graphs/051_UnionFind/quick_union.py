# Quick Union (with path compression)
# Union by Rank
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size+1)]
        self.rank = [1]*(size+1)
    
    # with path compression optimization
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    # quick union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            # union did not happen
            return False

        # union happened
        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)