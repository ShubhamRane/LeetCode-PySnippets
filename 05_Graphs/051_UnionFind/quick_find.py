# Quick Find
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x): # O(1)
        return self.root[x]
    
    def union(self, x, y): # O(N)
        rootX = self.find(x)
        rootY = self.find(y)
        
        n = len(self.root)
        for i in range(n):
            if self.root[i] == rootY:
                self.root[i] = rootX
    
    def connected(self, x, y): #  O(1)
        return self.find(x) == self.find(y)
    
    def getConnectedComponents(self):
        n = len(self.root)
        count = 0
        for i in range(n):
            if i == self.root[i]:
                count+=1
        return count