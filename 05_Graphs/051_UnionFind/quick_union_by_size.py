# Quick Union (with path compression)
# Union by Size
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size+1)]
        self.size = [1]*(size+1)
    
    # with path compression optimization
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            # union did not happen
            return False

        # union happened
        if self.size[rootX] > self.size[rootY]:
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.root[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)